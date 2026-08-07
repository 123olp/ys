(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.HumanInfraTimelineCore = factory();
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  const TIME_WINDOWS = {
    all: null,
    ancient: [-4000, -1],
    classical: [0, 500],
    medieval: [501, 1500],
    modern: [1501, 1900],
    twentieth: [1901, 2000],
    twentyfirst: [2001, 2100]
  };

  function esc(value) {
    return String(value == null ? "" : value).replace(/[&<>"']/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch];
    });
  }

  function dateLabel(event) {
    const start = event.start_date || {};
    let label = "";
    const year = start.year;
    if (year == null) return "";
    if (year < 0) {
      label = "公元前 " + Math.abs(year) + " 年";
      if (start.month != null) label += " " + start.month + " 月";
      if (start.day != null) label += " " + start.day + " 日";
      return label;
    }
    label = String(year);
    if (start.month != null) label += "-" + String(start.month).padStart(2, "0");
    if (start.day != null) label += "-" + String(start.day).padStart(2, "0");
    return label;
  }

  function displayWidth(value) {
    return Array.from(String(value == null ? "" : value)).reduce(function (width, ch) {
      const code = ch.codePointAt(0);
      if (
        (code >= 0x1100 && code <= 0x115f) ||
        (code >= 0x2e80 && code <= 0xa4cf) ||
        (code >= 0xac00 && code <= 0xd7a3) ||
        (code >= 0xf900 && code <= 0xfaff) ||
        (code >= 0xfe30 && code <= 0xfe4f) ||
        (code >= 0xff00 && code <= 0xff60) ||
        (code >= 0xffe0 && code <= 0xffe6)
      ) {
        return width + 2;
      }
      return width + 1;
    }, 0);
  }

  function padEnd(value, width) {
    let text = String(value == null ? "" : value).replace(/\s+/g, " ");
    const gap = width - displayWidth(text);
    if (gap > 0) text += " ".repeat(gap);
    return text;
  }

  function psqlTable(headers, rows) {
    const widths = headers.map(function (header, index) {
      let width = displayWidth(header);
      rows.forEach(function (row) {
        width = Math.max(width, displayWidth(row[index]));
      });
      return width;
    });
    const border = "+" + widths.map(function (width) {
      return "-".repeat(width + 2);
    }).join("+") + "+";
    function renderRow(row) {
      return "| " + widths.map(function (width, index) {
        return padEnd(row[index], width);
      }).join(" | ") + " |";
    }
    return [
      border,
      renderRow(headers),
      border,
      renderRow(rows[0] || []),
      border
    ].join("\n");
  }

  function renderPsqlTable(headers, rows) {
    if (!rows.length) return "";
    const widths = headers.map(function (header, index) {
      let width = displayWidth(header);
      rows.forEach(function (row) {
        width = Math.max(width, displayWidth(row[index]));
      });
      return width;
    });
    const border = "+" + widths.map(function (width) {
      return "-".repeat(width + 2);
    }).join("+") + "+";
    function renderRow(row) {
      return "| " + widths.map(function (width, index) {
        return padEnd(row[index], width);
      }).join(" | ") + " |";
    }
    return [
      border,
      renderRow(headers),
      border
    ].concat(rows.map(renderRow), [border]).join("\n");
  }

  function eventRow(event) {
    const meta = event.meta || {};
    return [
      event.text && event.text.headline ? event.text.headline : "",
      meta.event_id || "",
      dateLabel(event),
      meta.period_label || "",
      meta.path_family_label || meta.path_family || "",
      meta.event_type_label || meta.event_type || "",
      (meta.evidence_grade || "") + " / " + (meta.verification_status || ""),
      meta.publication_status === "selected" ? "作品子集" : "候选资料",
      (meta.source_refs || []).join(", ")
    ];
  }

  function unique(values) {
    return Array.from(new Set(values.filter(Boolean))).sort(function (a, b) {
      return String(a).localeCompare(String(b), "zh-Hans-CN");
    });
  }

  function plainText(event) {
    const meta = event.meta || {};
    return [
      event.text && event.text.headline,
      event.text && event.text.text ? event.text.text.replace(/<[^>]*>/g, " ") : "",
      meta.event_id,
      meta.period_label,
      meta.path_family,
      meta.event_type,
      meta.evidence_grade
    ].join(" ").toLowerCase();
  }

  function matchesEvent(event, state) {
    const meta = event.meta || {};
    const year = event.start_date && event.start_date.year != null ? event.start_date.year : 0;
    const windowRange = TIME_WINDOWS[state.window] || null;
    if (windowRange && (year < windowRange[0] || year > windowRange[1])) return false;
    if (state.scope === "works" && meta.publication_status !== "selected") return false;
    if (state.scope === "reviewed" && meta.verification_status !== "locally_reviewed") return false;
    if (state.period && meta.period_label !== state.period) return false;
    if (state.path && meta.path_family !== state.path) return false;
    if (state.type && meta.event_type !== state.type) return false;
    if (state.evidence && meta.evidence_grade !== state.evidence) return false;
    if (state.q) {
      const needle = String(state.q).toLowerCase();
      const haystack = event._searchText || plainText(event);
      if (haystack.indexOf(needle) < 0) return false;
    }
    return true;
  }

  return {
    TIME_WINDOWS,
    esc,
    dateLabel,
    displayWidth,
    padEnd,
    psqlTable,
    renderPsqlTable,
    eventRow,
    unique,
    plainText,
    matchesEvent
  };
});
