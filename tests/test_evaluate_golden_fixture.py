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
        self.assertFalse(report["domestic"]["accidental_cancellation"])

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


if __name__ == "__main__":
    unittest.main()
