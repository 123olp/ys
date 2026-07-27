(function () {
  "use strict";

  const root = document.documentElement;
  const storagePrefix = "human-infra-vector-clientpref-";
  const appearancePinnedFeature = "appearance-pinned";
  const appearanceBreakpoint = window.matchMedia("(min-width: 1120px)");
  const preferences = {
    "vector-feature-custom-font-size": {
      options: [ "0", "1", "2" ],
      fallback: "1"
    },
    "vector-feature-limited-width": {
      options: [ "1", "0" ],
      fallback: "1"
    },
    "skin-theme": {
      options: [ "os", "day", "night" ],
      fallback: "day"
    }
  };

  function classValue(feature, options) {
    const prefix = `${feature}-clientpref-`;
    const match = Array.from(root.classList).find((name) => {
      return name.startsWith(prefix) && options.includes(name.slice(prefix.length));
    });
    return match ? match.slice(prefix.length) : null;
  }

  function storedValue(feature, options) {
    try {
      const value = localStorage.getItem(storagePrefix + feature);
      return options.includes(value) ? value : null;
    } catch (_error) {
      return null;
    }
  }

  function apply(feature, value, persist) {
    const { options } = preferences[feature];
    for (const option of options) {
      root.classList.remove(`${feature}-clientpref-${option}`);
    }
    root.classList.add(`${feature}-clientpref-${value}`);
    if (persist) {
      try {
        localStorage.setItem(storagePrefix + feature, value);
      } catch (_error) {
        // The preference still applies for this page when storage is unavailable.
      }
    }
    window.dispatchEvent(new Event("resize"));
  }

  function applyAppearancePinned(desiredPinned, persist) {
    const appearance = document.getElementById("vector-appearance");
    const header = appearance?.querySelector(".vector-pinnable-header");
    const pinnedContainer = document.getElementById(
      "vector-appearance-pinned-container"
    );
    const unpinnedContainer = document.getElementById(
      "vector-appearance-unpinned-container"
    );
    if (!appearance || !header || !pinnedContainer || !unpinnedContainer) {
      return;
    }

    const actualPinned = desiredPinned && appearanceBreakpoint.matches;
    const target = actualPinned ? pinnedContainer : unpinnedContainer;
    if (appearance.parentElement !== target) {
      target.append(appearance);
    }
    root.classList.remove(
      "vector-feature-appearance-pinned-clientpref-0",
      "vector-feature-appearance-pinned-clientpref-1"
    );
    root.classList.add(
      `vector-feature-appearance-pinned-clientpref-${actualPinned ? "1" : "0"}`
    );
    header.classList.remove(
      "vector-pinnable-header-pinned",
      "vector-pinnable-header-unpinned"
    );
    header.classList.add(
      actualPinned
        ? "vector-pinnable-header-pinned"
        : "vector-pinnable-header-unpinned"
    );
    header.dataset.savedPinnedState = String(desiredPinned);
    if (persist) {
      try {
        localStorage.setItem(
          storagePrefix + appearancePinnedFeature,
          desiredPinned ? "1" : "0"
        );
      } catch (_error) {
        // The fixed state still applies for this page when storage is unavailable.
      }
    }
    window.dispatchEvent(new Event("resize"));
  }

  for (const [feature, config] of Object.entries(preferences)) {
    const value = storedValue(feature, config.options)
      || classValue(feature, config.options)
      || config.fallback;
    apply(feature, value, false);
    const input = document.getElementById(
      `skin-client-pref-${feature}-value-${value}`
    );
    if (input) input.checked = true;
  }

  const appearance = document.getElementById("vector-appearance");
  const pinButton = appearance?.querySelector(
    ".vector-pinnable-header-pin-button"
  );
  const unpinButton = appearance?.querySelector(
    ".vector-pinnable-header-unpin-button"
  );
  if (pinButton instanceof HTMLButtonElement) {
    pinButton.type = "button";
    pinButton.setAttribute("aria-label", "将外观移至侧栏");
  }
  if (unpinButton instanceof HTMLButtonElement) {
    unpinButton.type = "button";
    unpinButton.setAttribute("aria-label", "隐藏外观");
  }

  let desiredPinned = storedValue(
    appearancePinnedFeature,
    [ "0", "1" ]
  );
  desiredPinned = desiredPinned === null
    ? classValue(appearancePinnedFeature, [ "0", "1" ]) !== "0"
    : desiredPinned === "1";
  applyAppearancePinned(desiredPinned, false);

  pinButton?.addEventListener("click", () => {
    desiredPinned = true;
    const dropdown = document.getElementById(
      "vector-appearance-dropdown-checkbox"
    );
    if (dropdown instanceof HTMLInputElement) dropdown.checked = false;
    applyAppearancePinned(desiredPinned, true);
  });
  unpinButton?.addEventListener("click", () => {
    desiredPinned = false;
    applyAppearancePinned(desiredPinned, true);
  });
  appearanceBreakpoint.addEventListener("change", () => {
    applyAppearancePinned(desiredPinned, false);
  });

  appearance?.addEventListener(
    "change",
    (event) => {
      const input = event.target;
      if (!(input instanceof HTMLInputElement) || input.type !== "radio") return;
      for (const [feature, config] of Object.entries(preferences)) {
        if (input.name === `skin-client-pref-${feature}-group`
          && config.options.includes(input.value)) {
          apply(feature, input.value, true);
          return;
        }
      }
    }
  );
}());
