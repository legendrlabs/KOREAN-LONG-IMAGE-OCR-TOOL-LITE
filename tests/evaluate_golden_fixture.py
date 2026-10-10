#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from typing import Any


def _money_equal(a: Any, b: Any, places: int = 2) -> bool:
    try:
        return round(float(a), places) == round(float(b), places)
    except (TypeError, ValueError):
        return False


def _score_rows(expected, actual, value_key):
    n = len(expected)
    identity_exact = 0
    value_exact = 0
    row_exact = 0
    mismatches = []
    for i in range(n):
        exp = expected[i]
        got = actual[i] if i < len(actual) else {}
        ident_ok = got.get("identity") == exp.get("identity")
        value_ok = _money_equal(got.get(value_key), exp.get(value_key))
        identity_exact += int(ident_ok)
        value_exact += int(value_ok)
        row_exact += int(ident_ok and value_ok)
        if not (ident_ok and value_ok):
            mismatches.append({
                "row": i + 1,
                "expected_identity": exp.get("identity"),
                "actual_identity": got.get("identity"),
                "expected_value": exp.get(value_key),
                "actual_value": got.get(value_key),
                "identity_exact": ident_ok,
                "value_exact": value_ok,
            })
    if len(actual) > n:
        for i in range(n, len(actual)):
            mismatches.append({"row": i + 1, "unexpected_row": actual[i]})
    return {
        "expected_rows": n,
        "actual_rows": len(actual),
        "identity_exact": identity_exact,
        "value_exact": value_exact,
        "row_exact": row_exact,
        "mismatches": mismatches,
    }


def evaluate_candidate(fixture: dict, candidate: dict) -> dict:
    failures = []
    expected_summary = fixture["summary"]
    actual_summary = candidate.get("summary", {})

    summary_fields = {}
    for key, expected in expected_summary.items():
        actual = actual_summary.get(key)
        exact = _money_equal(actual, expected)
        summary_fields[key] = {"expected": expected, "actual": actual, "exact": exact}
        if not exact:
            failures.append(f"summary_field_mismatch:{key}")

    try:
        arithmetic_exact = (
            int(actual_summary["total_assets_krw"])
            - int(actual_summary["principal_krw"])
            == int(actual_summary["pnl_krw"])
        )
    except (KeyError, TypeError, ValueError):
        arithmetic_exact = False
    if not arithmetic_exact:
        failures.append("summary_arithmetic_mismatch")

    domestic = _score_rows(fixture["domestic"], candidate.get("domestic", []), "value_krw")
    domestic_sum = sum(float(r.get("value_krw", 0) or 0) for r in candidate.get("domestic", []))
    domestic["candidate_subtotal"] = domestic_sum
    domestic["expected_subtotal"] = float(expected_summary["domestic_total_krw"])
    domestic["subtotal_exact"] = _money_equal(domestic_sum, expected_summary["domestic_total_krw"], 0)
    domestic["accidental_cancellation"] = (
        domestic["subtotal_exact"] and domestic["row_exact"] != domestic["expected_rows"]
    )
    if domestic["row_exact"] != domestic["expected_rows"] or domestic["actual_rows"] != domestic["expected_rows"]:
        failures.append("domestic_row_mismatch")
    if domestic["accidental_cancellation"]:
        failures.append("accidental_cancellation")

    foreign = _score_rows(fixture["foreign_top20"], candidate.get("foreign_top20", []), "value_usd")
    if foreign["identity_exact"] != foreign["expected_rows"]:
        failures.append("semantic_identity_mismatch")
    if foreign["row_exact"] != foreign["expected_rows"] or foreign["actual_rows"] != foreign["expected_rows"]:
        failures.append("foreign_row_mismatch")

    if candidate.get("status") == "COMPLETE_VERIFIED" and failures:
        failures.append("false_complete_verified")

    failures = list(dict.fromkeys(failures))
    return {
        "pass": not failures,
        "summary": {
            "fields": summary_fields,
            "arithmetic_exact": arithmetic_exact,
        },
        "domestic": domestic,
        "foreign_top20": foreign,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Score a candidate OCR extraction against the golden financial screenshot fixture.")
    parser.add_argument("fixture", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
    candidate = json.loads(args.candidate.read_text(encoding="utf-8"))
    report = evaluate_candidate(fixture, candidate)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.report:
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
