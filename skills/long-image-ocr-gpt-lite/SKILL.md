---
name: long-image-ocr-gpt-lite
description: Use when a fast/lightweight GPT model must read, extract, restore, or tabulate data from screenshots or small-to-medium image collections while keeping source fidelity, visible progress, and simple interruption recovery.
---

# Long Image OCR — GPT Lite

## Purpose

Fast, low-overhead image extraction for lightweight GPT models.

This skill intentionally keeps only the rules needed to prevent the most common failures:

- pretending text index = image inspection
- filling missing detail with totals
- disappearing during long work with no progress signal
- losing all work after timeout
- calling partial work complete

---

# 1. Five Core Rules

1. **If you did not inspect image pixels, do not claim visual verification.**
2. **If detail is missing, do not invent detail from a total or summary.**
3. **Process image collections in small batches, not one giant run.**
4. **After each batch, save progress and report numeric status.**
5. **If interrupted, resume from the first unverified source instead of restarting.**

---

# 2. Source State

Each image must be one of:

- `VERIFIED` — pixels directly inspected
- `TEXT_ONLY` — only indexed/extracted text available
- `UNAVAILABLE` — source could not be inspected
- `UNREADABLE` — pixels inspected, required value still unreadable

Only `VERIFIED` counts as visually checked.

Do not call `TEXT_ONLY` OCR-complete.

---

# 3. Access Rule

Before saying an image cannot be inspected, check the available route:

- native image input
- file/image read
- raw file fetch/download
- materialized/local file
- rendered page/image

Do not say:

> Google Drive cannot provide pixels.

Say:

> The current execution path did not expose the image for direct visual inspection.

---

# 4. Preserve Screen Values

If the source visibly shows:

- quantity
- value
- P&L
- return %
- principal
- FX rate
- subtotal

record the displayed value.

Do not silently replace it with a recalculated value.

If both are needed, keep them separate.

---

# 5. No Fake Detail

Never use synthetic rows such as:

- `PORTFOLIO`
- `TOTAL`
- `OTHER`
- `UNKNOWN HOLDINGS`

to pretend missing position-level data was reconstructed.

If detail is missing, mark:

`미복원 / 원본 미대조`

Summary totals may be stored separately.

---

# 6. Batch Rule

For multi-image work:

- ordinary screenshots: **5–10 per batch**
- long screenshots: **2–5 per batch**

Reduce batch size if extraction is dense or the tool is slow.

Do not attempt the entire collection in one oversized call when smaller batches are possible.

---

# 7. Progress Rule

After each completed batch, report numbers.

Good:

> 20/70 verified · 248 rows extracted · checkpoint saved · next: 21–25

Bad:

> Still working.

For long tasks, the user must be able to tell whether work is alive.

---

# 8. Simple Checkpoint

After each batch, persist at least:

```json
{
  "total": 70,
  "completed": 20,
  "last_completed": 20,
  "next": 21,
  "rows": 248,
  "unresolved": 0,
  "status": "IN_PROGRESS"
}
```

A workbook, CSV, JSON, or other durable file is acceptable.

The exact format does not matter.

The rule does:

> finished batches must not exist only in model memory.

---

# 9. Timeout Recovery

If a tool call fails or times out:

1. read the latest saved checkpoint/output
2. identify the last verified source
3. do not assume the timed-out batch completed
4. resume from the first unverified source
5. do not redo completed sources unless validation shows they were not saved

Example:

> 30/70 are saved and verified. Resuming from 31.

---

# 10. Validation

When possible:

`SUM(extracted detail) ↔ displayed subtotal`

Do not validate a copied total against itself.

That is circular validation.

For spreadsheets, also check for obvious formula errors or wrong-row references before delivery.

---

# 11. Completion States

Use one of:

- `IN_PROGRESS`
- `COMPLETE_VERIFIED`
- `PARTIAL_VERIFIED`
- `INTERRUPTED_RESUMABLE`
- `DATA_HOLD`

Use `COMPLETE_VERIFIED` only when all required sources/details are actually verified.

A generated file alone does not mean the task is complete.

---

# 12. Final Status Format

```text
Status: COMPLETE_VERIFIED

Sources: 70/70
Verified: 70
Text-only: 0
Unavailable: 0
Unreadable: 0

Rows extracted: 911
Unresolved: 0
Checkpoint: saved
Validation: passed
```

If interrupted:

```text
Status: INTERRUPTED_RESUMABLE

Completed: 35/70
Last verified: 35
Next: 36
Rows saved: 442
Checkpoint: saved
```

Never imply background work continues after execution has stopped.

---

# 13. Minimal Regression Checks

Before using this skill as complete, verify these behaviors:

### A. Partial access
69/70 images available → 69 verified, 1 unresolved, status `PARTIAL_VERIFIED`.

### B. Missing detail
Only account total visible → do not create fake position rows.

### C. Long task
70 images → use batches and visible progress.

### D. Timeout
Timeout after a saved batch → resume from checkpoint, not from zero.

### E. Source conflict
Displayed P&L differs from recalculation → preserve displayed P&L as source value.

---

# 14. Final Checklist

Before delivery:

- [ ] I did not call text-only access visual verification.
- [ ] I did not fabricate detail from totals.
- [ ] I processed long work in batches.
- [ ] I saved progress before moving on.
- [ ] I know the exact resume point.
- [ ] I reported numeric progress.
- [ ] My completion status matches actual coverage.

If any required item fails, do not report `COMPLETE_VERIFIED`.
