#!/usr/bin/env python3
"""Regression tests for Crossref publication-date selection."""

from __future__ import annotations

import backfill_history_timeline_dates as date_backfill
import audit_history_timeline_quality as quality_audit


choose_date = date_backfill.choose_date
choose_date_record = date_backfill.choose_date_record


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(
        choose_date(
            {
                "published-online": {"date-parts": [[2024, 6, 12]]},
                "created": {"date-parts": [[2024, 6, 18]]},
            }
        )
        == "2024-06-12",
        "published_online_full_date_not_selected",
    )
    require(
        choose_date(
            {
                "published-print": {"date-parts": [[2024, 7]]},
                "published-online": {"date-parts": [[2024, 6]]},
                "issued": {"date-parts": [[2024, 7]]},
                "created": {"date-parts": [[2024, 6, 18]]},
            }
        )
        is None,
        "created_timestamp_must_not_be_used_as_publication_date",
    )
    require(
        choose_date({"created": {"date-parts": [[2024, 6, 18]]}}) is None,
        "created_only_record_must_not_produce_publication_date",
    )
    require(
        choose_date({"issued": {"date-parts": [[2024, 7, 3]]}}) == "2024-07-03",
        "issued_full_date_not_selected",
    )
    require(
        choose_date_record(
            {
                "published-online": {"date-parts": [[2024, 6]]},
                "published-print": {"date-parts": [[2024, 7, 3]]},
            }
        )
        == {
            "date": "2024-06",
            "precision": "month",
            "field": "published-online",
            "provenance": date_backfill.CACHE_PROVENANCE,
        },
        "online_publication_must_precede_later_print_precision",
    )
    require(
        choose_date_record({"published-online": {"date-parts": [[2024, 6]]}})
        == {
            "date": "2024-06",
            "precision": "month",
            "field": "published-online",
            "provenance": date_backfill.CACHE_PROVENANCE,
        },
        "month_precision_record_not_preserved",
    )
    require(
        getattr(date_backfill, "trusted_cache_date", lambda _entry: "untrusted")(
            "2024-07-03"
        )
        is None,
        "legacy_string_cache_must_not_be_trusted",
    )
    require(
        date_backfill.trusted_cache_date(
            {
                "date": "2024-07-03",
                "precision": "day",
                "field": "issued",
                "provenance": date_backfill.CACHE_PROVENANCE,
            }
        )
        == "2024-07-03",
        "versioned_publication_cache_not_accepted",
    )
    require(
        date_backfill.trusted_cache_record(
            {
                "date": "2024-07",
                "precision": "month",
                "field": "published-online",
                "provenance": date_backfill.CACHE_PROVENANCE,
            }
        )
        is not None,
        "trusted_month_precision_cache_not_accepted",
    )
    trusted_month = {
        "date": "2024-06",
        "precision": "month",
        "field": "published-online",
        "provenance": date_backfill.CACHE_PROVENANCE,
    }
    require(
        not date_backfill.event_needs_refresh(
            {
                "date_start": "2024-06",
                "date_type": "approx",
                "notes": "日期补齐：Crossref 2024-06 (published-online, month, v3)",
            },
            "10.0000/example",
            {"10.0000/example": trusted_month},
            True,
        ),
        "current_versioned_month_record_must_be_idempotent",
    )
    require(
        date_backfill.event_needs_refresh(
            {"date_start": "2024-06-18", "date_type": "exact", "notes": "旧记录"},
            "10.0000/example",
            {"10.0000/example": "2024-06-18"},
            True,
        ),
        "legacy_cache_without_note_marker_must_be_refetched",
    )
    event = {
        "date_start": "2024-06",
        "date_type": "approx",
        "notes": "日期补齐：Crossref 2024-06 (published-online, month, v3)",
        "updated_at": "2024-07-01T00:00:00Z",
    }
    require(
        not date_backfill.apply_date_record(
            event,
            trusted_month,
            "2024-08-01T00:00:00Z",
        ),
        "identical_record_must_not_rewrite_event",
    )
    require(
        event["updated_at"] == "2024-07-01T00:00:00Z",
        "idempotent_update_must_preserve_event_timestamp",
    )
    require(
        quality_audit.event_is_future("2026-09", "2026-08-08"),
        "future_month_must_be_rejected",
    )
    require(
        not quality_audit.event_is_future("-2353~", "2026-08-08"),
        "historical_approximate_date_must_not_be_treated_as_future",
    )
    require(
        quality_audit.event_has_untrusted_crossref_date(
            {"sources": ["SRC-1"], "notes": "旧记录"},
            {"SRC-1": {"doi": "10.0000/example"}},
            {"10.0000/example": "2024-06-18"},
        ),
        "legacy_cache_without_note_marker_must_fail_quality_audit",
    )
    require(
        not quality_audit.event_has_untrusted_crossref_date(
            {
                "sources": ["SRC-1"],
                "notes": "日期补齐：Crossref 2024-06 "
                "(published-online, month, v3)",
            },
            {"SRC-1": {"doi": "10.0000/example"}},
            {"10.0000/example": trusted_month},
        ),
        "trusted_cache_record_must_pass_quality_audit",
    )
    print("status=OK history_timeline_dates=pass")


if __name__ == "__main__":
    main()
