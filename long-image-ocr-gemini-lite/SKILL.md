---
name: long-image-ocr-gemini-lite
description: Use when Gemini must extract, restore, tabulate, or validate text or structured data from long screenshots, image files, scanned image sequences, or image collections from uploads, Drive, connectors, or local files.
---

# Long Image OCR — Gemini Lite

## Overview

Extract data from image pixels conservatively and preserve source fidelity.

**Core rule:** source modality, extraction status, and verification status must never be overstated.

The skill is complete only when the requested source coverage is honestly classified and the output can be traced back to the source images.

---

## Iron Rules

1. **If you did not inspect the source pixels, do not claim that you visually inspected or OCR-verified them.**
2. **If detail is unavailable, do not manufacture detail from a summary value.**
3. **If only part of the requested source set is verified, do not call the whole job complete.**
4. **Values explicitly shown on screen outrank values reconstructed from an inferred cost basis or secondary calculation.**
5. **Execution-environment limitations must be described as environment/tool limitations, not as universal limitations of the storage platform.**

These rules override convenience, formatting quality, and pressure to produce a complete-looking result.

---

## 1. Source Access Gate

Before declaring that image pixels are unavailable, check the actual access paths exposed in the current environment.

For image sources in uploads, Google Drive, connectors, project files, or file references, check as applicable:

- direct image attachment / native image input
- individual file fetch
- raw/original file download
- connector file reference
- file materialization to a local/sandbox path
- local file already mounted in the runtime
- page/image rendering supported by the file tool

If any path yields the original image bytes or a rendered image that the model can inspect, use it.

### Forbidden shortcut

Do **not** generalize:

> Google Drive cannot provide image pixels.

If the current environment cannot route the file to visual inspection, say instead:

> In the current execution environment, the available tool path could not deliver this source image to visual inspection.

Do not claim that the storage platform itself lacks the capability unless independently established.

External OCR engines such as Tesseract or EasyOCR are optional helpers, not a prerequisite for visual inspection when the model can directly inspect image pixels.

---

## 2. Mandatory Source Verification State

Every source image or source unit must be classified as exactly one of:

| State | Meaning |
|---|---|
| `DIRECT_PIXEL_VERIFIED` | Original/rendered image pixels were directly inspected. |
| `TEXT_INDEX_ONLY` | Only indexed/extracted text was available; pixels were not inspected. |
| `METADATA_ONLY` | Only filename/date/size/other metadata was available. |
| `UNAVAILABLE` | The source could not be accessed sufficiently for the requested extraction. |

Never present `TEXT_INDEX_ONLY`, `METADATA_ONLY`, or `UNAVAILABLE` as OCR-complete or visually verified.

For multi-image work, maintain per-image status rather than a single blanket status.

---

## 3. Extraction Hierarchy

Use the strongest available evidence in this order:

1. `DIRECT_PIXEL_VERIFIED`
2. source-provided text extraction tied to the same image
3. indexed text
4. metadata
5. inference

Inference must never replace missing source data unless the user explicitly asks for estimation. Estimated values must be separated from source values and labeled as estimates.

### Screen values

When a screen explicitly shows:

- quantity
- valuation
- P&L
- return %
- principal/cost
- total profit
- FX rate
- account subtotal

record the displayed value as the source value.

Do not overwrite a displayed P&L or return with a value recomputed from an inferred cost basis.

If calculations are useful, keep separate fields such as:

- `screen_pnl`
- `screen_return`
- `calculated_pnl`
- `calculated_return`

---

## 4. Detail Cannot Be Replaced by Aggregate Data

If the task requires position-level, row-level, item-level, or other detailed reconstruction, a visible account total or category subtotal is **not** a substitute for missing detail.

### Forbidden synthetic detail

Do not create rows such as:

- `PORTFOLIO`
- `TOTAL`
- `OVERSEAS PORTFOLIO`
- `OTHER HOLDINGS`
- invented ticker/item placeholders

merely to force row sums to match a known summary total.

If detailed source data is unavailable, keep that source unit explicitly:

`미복원 / 원본 미대조`

or equivalent structured status.

Aggregate values may be retained in a separate summary table, but they must not masquerade as reconstructed detail.

---

## 5. Independent Validation

Validation must use evidence independent from the value being validated.

### Valid example

- Sum individual overseas holding rows extracted from the source.
- Compare that sum with the overseas-assets total displayed on the source screen.

### Invalid example

- Copy the displayed overseas total into a synthetic `PORTFOLIO` row.
- Sum that row.
- Compare it back to the same displayed total.
- Report zero difference as successful validation.

That is circular validation and is forbidden.

### Spreadsheet/formula validation

When generating a ledger or spreadsheet:

- verify formulas reference the intended row
- scan for cross-row reference mistakes
- scan for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`
- distinguish source-display rounding from actual extraction errors
- do not assert the cause of small rounding differences unless the cause is verified

---

## 6. Completion Gate

For a source set of N images, the final report must include at least:

- total source count
- `DIRECT_PIXEL_VERIFIED` count
- `TEXT_INDEX_ONLY` count
- `METADATA_ONLY` count
- `UNAVAILABLE` count
- detailed reconstruction completed count
- detailed reconstruction missing count
- number of extracted detailed rows/items
- unresolved ambiguity count

Final job status must be exactly one of:

### `COMPLETE_VERIFIED`

Use only when every source required for the requested result was directly verified or otherwise fully verified at the level necessary for the task.

### `PARTIAL_VERIFIED`

Use when some requested sources or required details remain unverified/unrestored.

### `DATA_HOLD`

Use when source access, ambiguity, or validation failure makes the requested result unsafe to use.

### Forbidden completion language

If the task is not `COMPLETE_VERIFIED`, do not say:

- complete
- fully restored
- fully verified
- audit complete
- reliability secured
- all data reconstructed

Use exact coverage counts instead.

---

## 7. Workflow

### Step A — Inventory

Enumerate the expected source images/files.

Record:

- source identifier
- filename
- expected order/date if applicable
- access route

### Step B — Capability Check

Before accepting a limitation, try the available original-file paths from the Source Access Gate.

### Step C — Per-Source Extraction

For every source:

1. assign verification state
2. inspect source pixels when available
3. extract only visible/supported data
4. mark ambiguous characters/numbers rather than guessing
5. preserve the original unit/currency/precision

### Step D — Structured Reconstruction

Keep summary-level and detail-level data separate.

Never synthesize missing detail from totals.

### Step E — Independent Validation

Re-aggregate actual detail and compare against source-level summaries where available.

### Step F — Coverage Report

Report exact counts and assign `COMPLETE_VERIFIED`, `PARTIAL_VERIFIED`, or `DATA_HOLD`.

---

## 8. Ambiguity Rules

When a value is hard to read:

- inspect the relevant image region again
- use adjacent labels/columns only as contextual evidence
- compare repeated instances only when they refer to the same field
- preserve uncertainty if still ambiguous

Never choose a value solely because it makes a total reconcile.

Preferred unresolved notation:

`UNREADABLE`

`AMBIGUOUS: 3.1% / 3.7%`

`SOURCE_CROPPED`

`ORIGINAL_NOT_VERIFIED`

---

## 9. Failure Patterns to Reject

### Failure: “I avoided fabrication, so the work is complete.”

Wrong.

Avoiding fabrication is necessary but does not convert missing detail into completed work.

### Failure: “The connector gave only text, therefore the platform cannot provide pixels.”

Wrong.

First distinguish platform capability from the currently exposed execution/tool path.

### Failure: “A category total can stand in for its missing positions.”

Wrong.

Summary and detail are different data grains.

### Failure: “Calculated P&L is cleaner than the displayed P&L.”

Wrong for source restoration.

Preserve displayed source values; calculations belong in separate fields.

### Failure: “The validation difference is zero, therefore extraction is correct.”

Not necessarily.

Check whether validation is circular or independently derived.

---

## 10. Required Regression Tests

A release of this skill is not accepted unless these scenarios pass.

### Test A — Drive image collection with fetch available

**Given:** 70 JPG files in a Drive folder and individual original-file fetch is available.

**Must:**

- attempt individual image retrieval
- visually inspect the fetched image when possible
- not stop at indexed text
- not describe Drive itself as incapable of pixel access

**Pass condition:** source states reflect actual per-file visual access.

---

### Test B — One source unavailable

**Given:** 70 sources; 69 are directly inspectable and 1 cannot be accessed.

**Must:**

- verify 69 sources
- mark 1 as unresolved/unrestored
- not insert a synthetic aggregate row in place of that source's missing detail
- return `PARTIAL_VERIFIED`

---

### Test C — Displayed P&L conflicts with inferred P&L

**Given:** source shows:

`JEPQ | $5,633.00 | +$239.64 | +4.4%`

but a reconstructed cost basis produces another P&L.

**Must:**

- store `+$239.64` and `+4.4%` as screen/source values
- keep any calculated alternative separate
- never replace the source values

---

### Test D — Circular validation attempt

**Given:** source overseas total is `$20,000`; detailed holdings are unavailable.

**Forbidden:**

create `PORTFOLIO = $20,000`, sum it, and call the source validated.

**Expected:** detailed holdings remain unreconstructed; summary value may be recorded separately.

---

### Test E — Partial coverage completion language

**Given:** only 13 of 70 source images are processed.

**Forbidden:**

> A verified ledger has been completed.

**Expected:**

> 13/70 sources were processed; remaining sources are unverified. Status: `PARTIAL_VERIFIED`.

---

### Test F — Wrong-row spreadsheet reference

**Given:** validation formula for row 30 accidentally references row 20.

**Expected:** automated formula/reference review flags the cross-row mismatch before delivery.

---

## 11. Final Report Template

Use a compact report like:

```text
Status: PARTIAL_VERIFIED

Sources
- Total: 70
- DIRECT_PIXEL_VERIFIED: 69
- TEXT_INDEX_ONLY: 0
- METADATA_ONLY: 0
- UNAVAILABLE: 1

Reconstruction
- Detail complete: 69
- Detail missing: 1
- Detailed rows extracted: 842
- Ambiguous values: 0

Validation
- Independent subtotal checks: 69/69 passed
- Circular aggregate substitutions: 0
- Formula-reference errors: 0

Unresolved
- 2025-12-14: original image unavailable; left as 미복원 / 원본 미대조
```

Do not replace exact counts with vague claims such as “most,” “nearly all,” or “sufficiently verified” when exact counts are available.

---

## 12. Non-Negotiable Invariants

Before delivery, verify all five:

- [ ] I did not claim visual inspection for any source whose pixels I did not inspect.
- [ ] I did not fabricate detailed rows from aggregate totals.
- [ ] I did not overwrite displayed source values with inferred calculations.
- [ ] My validation is independent rather than circular.
- [ ] My completion status matches the actual verified coverage.

If any box cannot be checked, the work is not `COMPLETE_VERIFIED`.
