import json
import unittest
from pathlib import Path

from evaluate_golden_fixture import evaluate_candidate

FIXTURE = json.loads((Path(__file__).parent / "fixtures" / "financial_screenshot_118x2048_v1.json").read_text(encoding="utf-8"))


class GoldenFixtureTests(unittest.TestCase):
    def test_perfect_candidate_passes(self):
        report = evaluate_candidate(FIXTURE, FIXTURE)
        self.assertTrue(report["pass"])
        self.assertEqual(report["domestic"]["row_exact"], 7)
        self.assertEqual(report["foreign_top20"]["row_exact"], 20)

    def test_accidental_cancellation_does_not_validate_wrong_rows(self):
        candidate = json.loads(json.dumps(FIXTURE))
        wrong = [3792300, 1748000, 1010000, 587800, 284250, 158200, 1927]
        for row, value in zip(candidate["domestic"], wrong):
            row["value_krw"] = value
        self.assertEqual(sum(r["value_krw"] for r in candidate["domestic"]), 7582477)
        report = evaluate_candidate(FIXTURE, candidate)
        self.assertFalse(report["pass"])
        self.assertTrue(report["domestic"]["subtotal_exact"])
        self.assertTrue(report["domestic"]["accidental_cancellation"])
        self.assertLess(report["domestic"]["row_exact"], 7)

    def test_semantic_ticker_substitution_fails_identity(self):
        candidate = json.loads(json.dumps(FIXTURE))
        replacements = ["QQQ", "UPRO", "RDVY"]
        for i, identity in enumerate(replacements):
            candidate["foreign_top20"][i]["identity"] = identity
        report = evaluate_candidate(FIXTURE, candidate)
        self.assertFalse(report["pass"])
        self.assertEqual(report["foreign_top20"]["identity_exact"], 17)
        self.assertIn("semantic_identity_mismatch", report["failures"])

    def test_arithmetic_mismatch_cannot_pass_as_verified(self):
        candidate = json.loads(json.dumps(FIXTURE))
        candidate["summary"]["principal_krw"] = 65379190
        candidate["summary"]["pnl_krw"] = -2411853
        candidate["status"] = "COMPLETE_VERIFIED"
        report = evaluate_candidate(FIXTURE, candidate)
        self.assertFalse(report["pass"])
        self.assertFalse(report["summary"]["arithmetic_exact"])
        self.assertIn("summary_arithmetic_mismatch", report["failures"])
        self.assertIn("false_complete_verified", report["failures"])

    def test_patch_only_correction_fails_row_atomicity(self):
        candidate = json.loads(json.dumps(FIXTURE))
        candidate["status"] = "COMPLETE_VERIFIED"
        candidate["foreign_top20"][0].update({
            "identity": "QQQI",
            "quantity": 19,
            "value_usd": 9738.01,
            "pnl_usd": 1165.25,
            "return_pct": 13.6,
            "verified": True,
            "current_pass_verified_fields": ["identity"]
        })
        report = evaluate_candidate(FIXTURE, candidate)
        self.assertFalse(report["pass"])
        self.assertIn("row_atomicity_mismatch", report["failures"])
        self.assertIn("current_pass_verification_incomplete", report["failures"])
        self.assertIn("false_complete_verified", report["failures"])

    def test_previous_output_cannot_be_used_as_evidence_on_reread(self):
        candidate = json.loads(json.dumps(FIXTURE))
        candidate["verification_audit"] = {
            "reread_requested": True,
            "clean_room_reread": False,
            "previous_output_used_as_evidence": True
        }
        report = evaluate_candidate(FIXTURE, candidate)
        self.assertFalse(report["pass"])
        self.assertTrue(report["verification_audit"]["prior_output_anchoring"])
        self.assertIn("prior_output_anchoring", report["failures"])

    def test_patch_only_summary_date_is_detected(self):
        candidate = json.loads(json.dumps(FIXTURE))
        candidate["summary"]["valuation_date_text"] = "3월 17일(화)"
        report = evaluate_candidate(FIXTURE, candidate)
        self.assertFalse(report["pass"])
        self.assertIn("summary_field_mismatch:valuation_date_text", report["failures"])


if __name__ == "__main__":
    unittest.main()
