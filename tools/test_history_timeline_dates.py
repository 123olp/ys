#!/usr/bin/env python3
"""Regression tests for Crossref publication-date selection."""

from __future__ import annotations

import backfill_history_timeline_dates as date_backfill


choose_date = date_backfill.choose_date


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
                "provenance": date_backfill.CACHE_PROVENANCE,
            }
        )
        == "2024-07-03",
        "versioned_publication_cache_not_accepted",
    )
    print("status=OK history_timeline_dates=pass")


if __name__ == "__main__":
    main()
