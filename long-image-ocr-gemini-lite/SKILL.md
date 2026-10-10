---
name: long-image-ocr-gemini-lite
description: Use when Gemini must read, transcribe, extract, restore, tabulate, or validate text or structured data from long screenshots, dense document images, tables, transaction histories, chats, logs, Drive image collections, or other OCR-sensitive visual content.
---

# Long Image OCR — Gemini Lite

## Purpose

An **instruction-only, evidence-only native-vision protocol** for Gemini.

Use only vision, file, connector, rendering, and inspection operations the current host actually exposes. Do **not** invoke or claim to invoke external OCR engines, Python/MCP processes, APIs, Cloud Run, local executables, image-slicing programs, EasyOCR/Tesseract, or a `GEMINI_API_KEY` application unless the user explicitly supplied and requested them.

**Core rule:** visible evidence beats plausibility; uncertainty beats guessing; missing evidence beats invented data.

## 0. Critical gates

Every extracted character, number, date, transaction, product, row, field, or record must be supported by source evidence.

1. If source pixels were not inspected, do not claim visual/OCR verification.
2. **Reconstruction is not completion.** Never fill gaps to make a sequence look complete.
3. Recurring patterns are not evidence. Never create missing records from repetition or expectation.
4. Missing evidence must remain missing; mark uncertainty instead of guessing.
5. Displayed source values outrank inferred/recomputed values for source restoration.
6. Partial source coverage must never be described as complete.
7. Execution-environment limits are environment/tool limits, not universal storage-platform limits.
8. **Verification is a gate, not the deliverable.** After verification, continue to the requested table, ledger, spreadsheet, transcription, or other output.
9. **Literal identity is locked.** Proper nouns and identifiers must be transcribed from visible glyphs, not replaced by more familiar domain entities.
10. **Arithmetic mismatch is a verification failure signal.** Reinspect before finalizing; do not explain it away without explicit source evidence.
11. **Row correctness comes before aggregate agreement.** A matching subtotal cannot validate incorrect, uncertain, shifted, or fabricated rows.
12. **Re-read means clean-room re-read.** When correcting or re-validating prior OCR, previous model output is not source evidence.
13. **Rows are atomic evidence units.** If any reported field in a row is corrected or re-read, re-read every reported field in that row from source pixels.
14. **VERIFIED is current-pass only.** Never inherit verification status from a previous answer or from a partially corrected row.

## 1. Source modality gate

Before reading an image, identify what is actually available:

- original/rendered **image pixels**
- source-provided OCR/extracted text tied to the image
- Drive/workspace **indexed text**
- metadata only
- no usable access

Before declaring pixels unavailable, check applicable routes: direct image input, individual fetch, raw/original download, connector file reference, materialization/local file, or page/image rendering.

If any route yields inspectable pixels, use them.

Do not generalize:

> Google Drive cannot provide image pixels.

Say instead:

> In the current execution environment, the available tool path could not deliver this source image to visual inspection.

Empty indexed text does not mean an image is unreadable. Do not claim crop, zoom, enhancement, or reinspection unless it actually occurred.

## 2. Mandatory per-source state

Every source image/page must be exactly one of:

| State | Meaning |
|---|---|
| `DIRECT_PIXEL_VERIFIED` | Original/rendered pixels were directly inspected. |
| `TEXT_INDEX_ONLY` | Only indexed/extracted text was available; pixels were not inspected. |
| `METADATA_ONLY` | Only metadata was available. |
| `UNAVAILABLE` | Source access was insufficient for the requested task. |

If pixels were inspected but a value remains unreadable, keep the source `DIRECT_PIXEL_VERIFIED` and mark the value `UNREADABLE` or `AMBIGUOUS`.

Never present non-pixel states as visually verified. Maintain state per source, not as a blanket status.

## 3. Source coverage gate

For multi-image/page work, maintain a coverage checklist.

Before claiming completion:

- inspect every accessible provided source;
- do not stop after a readable subset;
- do not skip similar-looking files;
- do not substitute indexed text for visual inspection when pixels are available;
- do not silently omit empty-index sources;
- record unavailable/unresolved sources explicitly.

Prefer exact counts over “most” or “nearly all.”

## 4. Evidence hierarchy and screen values

Evidence priority:

1. `DIRECT_PIXEL_VERIFIED`
2. source-provided text extraction tied to the same image
3. indexed text
4. metadata
5. inference

Inference may not replace missing source data unless the user asks for estimation.

Preserve visibly displayed quantity, valuation, P&L, return %, principal/cost, FX rate, subtotal, timestamp, and similar fields as source values. Do not silently overwrite them with calculations. If both are useful, keep `screen_*` and `calculated_*` fields separate.

## 5. Literal Identity Lock

For stock tickers, company names, fund names, product names, account names, usernames, identifiers, codes, and other proper nouns:

- transcribe the **visible glyphs literally**;
- never replace an unfamiliar or blurry identity with a more familiar one;
- never use domain knowledge as visual evidence;
- do not normalize a source identity unless the user explicitly asks for normalization after transcription;
- if unresolved, use `AMBIGUOUS: A / B` or `UNREADABLE`.

Forbidden examples:

- `QQQI → QQQ`
- `GPIQ → UPRO`
- `ROCQ → RDVY`
- an unfamiliar Korean company name → a better-known company with a similar silhouette

**Knowledge may trigger reinspection, never replacement.**

An unusual-but-visible ticker is preferable to a fabricated familiar ticker.

### Confidence must follow evidence

Do not label an identity or value as high-confidence, “양호,” clear, verified, or equivalent when:

- glyphs are blurred/compressed;
- multiple readings remain plausible;
- the model relied on familiarity/context to resolve it;
- arithmetic or cross-field checks contradict it.

Confidence labels must describe the visual evidence, not how plausible the answer feels.

## 6. No fake detail

Totals are not substitutes for missing position/item/transaction detail.

Do not create synthetic rows such as:

- `PORTFOLIO`
- `TOTAL`
- `OVERSEAS PORTFOLIO`
- `OTHER HOLDINGS`
- invented ticker/item placeholders

to force reconciliation.

Unavailable detail stays:

`미복원 / 원본 미대조`

Summary values may be stored separately, but must not masquerade as reconstructed detail.

## 7. Seven-phase workflow

### Phase 1 — Layout reconnaissance
Inspect the whole source for headings, tables, columns, cards, repeated rows, transaction groups, chats/logs, timelines, and dense regions. Establish visible order.

### Phase 2 — Segmented reading
Read long/dense sources in ordered logical regions using semantic boundaries. If a material region cannot be inspected reliably, mark `[not verified]`.

### Phase 3 — Boundary reconciliation
At region/screenshot boundaries check split rows, repeated headers, truncated values, skipped transitions, and overlap duplicates. Remove only overlap duplicates; preserve genuine repeated records.

### Phase 4 — Precision pass
Recheck dates, timestamps, amounts, prices, quantities, percentages, tickers, identifiers, and row/column associations. Never resolve conflicting digits by intuition. Apply the Literal Identity Lock to proper nouns and identifiers.

### Phase 5 — Low-confidence pass
Treat tiny text, blur, compression, low contrast, clipping, overlays, and look-alike characters as low confidence. Revisit only with real host capabilities. Use `UNREADABLE`, `AMBIGUOUS: A / B`, `SOURCE_CROPPED`, or `ORIGINAL_NOT_VERIFIED` when unresolved.

### Phase 6 — Reconstruction
Reassemble only source-supported information. Preserve order, chronology, relationships, grouping, and legitimate repetition. Never invent data for completeness.

### Phase 7 — Audit
Check source coverage, overlap duplicates, missing rows, numeric transcription, row/column shifts, literal identities, row-level correctness, uncertainty, traceability, arithmetic consistency, aggregate reconciliation, and spreadsheet/formula errors when applicable.

## 8. Structured output safety

For tables, ledgers, CSV, and spreadsheets:

- preserve field boundaries and row/column associations;
- verify each structured row independently;
- never build CSV by blindly joining fields with commas;
- quote/escape CSV fields containing commas, quotes, or newlines;
- use native spreadsheet cells for workbooks;
- ensure commas inside names/notes/filenames do not shift columns;
- scan for `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`;
- check wrong-row/cross-row formula references.

## 9. Clean-room Re-read and Row Atomicity Lock

When the user asks to re-read, re-validate, correct, audit, or retry an OCR result after a previous extraction was wrong or disputed, perform a **clean-room visual pass**.

### Clean-room Re-read

For the requested scope:

- discard the previous OCR extraction as a data source;
- re-read every requested field directly from the currently accessible source pixels;
- do not copy unchanged values from the previous table merely because the user did not mention them;
- do not use prior OCR values, prior guesses, prior corrections, or previous `VERIFIED` labels as evidence;
- use prior output only **after** the independent re-read, for comparison, diffing, and regression analysis.

A correction request is not permission to patch the previous answer cell-by-cell.

If source pixels needed for the clean-room pass are not accessible, say so and downgrade the result instead of preserving old values as if re-verified.

### Prior Output Anchoring / Patch-Only Correction

Forbidden pattern:

`previous answer → edit only user-identified cells → preserve untouched old cells → declare re-verified`

This is a protocol failure even when the corrected cells themselves are now accurate.

### Row Atomicity Lock

A structured row is an **atomic evidence unit**. If any field in a row is corrected, uncertain, contradicted, or re-read, re-read the entire reported row from source pixels, including every field that will appear in the final output, such as:

- identity / ticker / company / product name;
- quantity;
- valuation / amount;
- profit or loss;
- return percentage;
- currency, price, labels, and other row-associated fields.

Never correct only one field while carrying forward unverified values from a previous extraction.

Example of a forbidden patch-only row:

`QQQ → QQQI` while preserving previous `19 shares / $9,738.01 / +$1,165.25 / +13.6%`.

A row may be marked `VERIFIED` only when **every field actually reported for that row** was independently observed in the **current visual pass**.

### Current-pass Verification

`VERIFIED` means verified in the current visual pass.

- do not inherit row verification from a previous answer;
- do not inherit field confidence from a previous answer;
- do not mark the row verified because one corrected field was re-read;
- if some reported fields were not re-observed, mark the row partial/ambiguous or omit unverified fields as appropriate.

## 10. Row-First Validation and Accidental Cancellation Guard

Validate detailed rows **before** using any aggregate or subtotal as supporting evidence.

For each row, independently verify the fields that matter to the task, including when present:

- row identity/name/ticker;
- numeric value/amount;
- quantity/price/currency;
- row order and row-to-value association;
- confidence/ambiguity state.

Only after row-level checks are complete may totals or subtotals be used as a **secondary cross-check**.

A correct aggregate does **not** prove the rows are correct. Independent row errors can cancel each other and produce the exact displayed subtotal.

### Accidental cancellation guard

If:

`SUM(extracted rows) == displayed subtotal`

but one or more rows remain incorrect, uncertain, shifted, or unresolved:

- do not upgrade those rows to verified;
- do not describe the aggregate match as proof of OCR correctness;
- flag the result as possible `ACCIDENTAL_CANCELLATION` when useful for audit/reporting;
- keep the task `PARTIAL_VERIFIED` or `DATA_HOLD` when the unresolved row errors are material.

Never increase row confidence merely because the final sum matches.

**Validation order:**

`row identity/value/association → row confidence → aggregate calculation → displayed subtotal cross-check`

not:

`subtotal matches → therefore rows are correct`.

## 11. Arithmetic Consistency Gate

When a screen displays fields with an explicit arithmetic relationship, use that relationship as an independent verification check.

Common financial examples:

- `total assets - principal = displayed P&L`
- `principal + displayed P&L = total assets`
- `P&L / principal ≈ displayed return %` as a **secondary** check because display rounding may apply
- sum of extracted position values ↔ displayed category subtotal

If a material arithmetic relationship fails:

1. do **not** mark the affected values verified;
2. reinspect the relevant numeric region;
3. check digit grouping, sign, decimal point, currency, and row association;
4. if unresolved, mark the conflicting fields `AMBIGUOUS` or `UNREADABLE`;
5. downgrade final status to `PARTIAL_VERIFIED` or `DATA_HOLD` when material.

### No reconciliation storytelling

Never explain an arithmetic mismatch as:

- fees
- expenses
- taxes
- rounding
- FX effects
- settlement timing
- “제비용”
- any other reconciliation story

unless the **source explicitly provides evidence** for that explanation.

A plausible explanation is not validation.

Do not change source values merely to force the arithmetic to match; reinspect first and preserve uncertainty when unresolved.

## 12. Summary and independent validation

Recompute every summary, total, count, monthly rollup, or yearly rollup from the **final structured rows** after row-level validation.

Make explicit include/exclude decisions for overlap duplicates, cancellations/reversals, funding/top-ups, free/zero-value rows, and other non-counted evidence.

Valid:

`verified row detail → SUM(actual extracted detail) ↔ displayed source subtotal`

Invalid circular validation:

copy displayed subtotal → synthetic row → sum same row → compare to original subtotal → declare success.

Invalid aggregate-first validation:

wrong/uncertain rows → errors cancel → subtotal matches → declare rows verified.

Zero difference does not prove correctness when validation is circular or when row errors cancel.

## 13. Operating modes

### Auto
Default. Apply the full protocol for long, dense, repetitive, tabular, financial, or precision-sensitive sources.

### Exact transcription
Preserve visible wording/order. Do not silently autocorrect, normalize, or summarize unless asked. Apply Literal Identity Lock. Mark uncertainty explicitly.

### Structured extraction
Verify every row independently, preserve associations, never move values between rows, never create missing rows, preserve genuine duplicates, and normalize only when requested.

## 14. Completion gate

Final status must be exactly one of:

- `COMPLETE_VERIFIED`
- `PARTIAL_VERIFIED`
- `DATA_HOLD`

`COMPLETE_VERIFIED`: every source required for the requested result was verified at the necessary level in the current pass, with no unresolved material row, arithmetic, identity, clean-room, or provenance conflicts.

`PARTIAL_VERIFIED`: some requested sources/details remain unverified or unrestored.

`DATA_HOLD`: access, ambiguity, arithmetic inconsistency, identity uncertainty, row-level inconsistency, prior-output anchoring, incomplete current-pass verification, or other validation failure makes the result unsafe to use.

When relevant, report:

- total sources
- `DIRECT_PIXEL_VERIFIED`
- `TEXT_INDEX_ONLY`
- `METADATA_ONLY`
- `UNAVAILABLE`
- detail complete / missing
- extracted rows/items
- unresolved ambiguities
- row-level mismatches
- arithmetic mismatches still open
- possible accidental cancellation
- prior-output anchoring / patch-only correction detected
- current-pass incomplete rows

If status is not `COMPLETE_VERIFIED`, do not say complete, fully restored, fully verified, audit complete, all data reconstructed, or nothing missing.

## 15. Regression checks

A release must preserve these behaviors:

- **Drive pixels available:** inspect pixels; do not stop at indexed text.
- **69/70 available:** verify 69, mark 1 unresolved, no synthetic detail, `PARTIAL_VERIFIED`.
- **Displayed P&L conflicts with calculation:** preserve displayed source value; keep calculation separate.
- **Subtotal exists but detail missing:** no synthetic subtotal row or circular validation.
- **13/70 processed:** report 13/70 and `PARTIAL_VERIFIED`, not completion.
- **Wrong-row formula:** flag before delivery.
- **CSV field contains comma/quote/newline:** quote/escape without shifting columns.
- **Literal ticker identity:** visible `QQQI`, `GPIQ`, `ROCQ` must not be replaced with `QQQ`, `UPRO`, `RDVY` merely because those are more familiar.
- **Unknown identity:** if a ticker/company name remains blurry, return `AMBIGUOUS`/`UNREADABLE`; do not select a familiar security from context.
- **Financial arithmetic consistency:** if source reads assets `62,966,337`, principal `65,578,190`, and P&L `-2,611,853`, verify that `62,966,337 - 65,578,190 = -2,611,853`.
- **Arithmetic contradiction:** a reading such as principal `65,379,190` with the same assets/P&L must trigger reinspection or uncertainty, not a “fees/expenses” explanation.
- **Confidence discipline:** a blurry identity cannot be labeled “양호” merely because the chosen ticker/name is plausible.
- **Accidental cancellation:** domestic row values `3,792,300 + 1,748,000 + 1,010,000 + 587,800 + 284,250 + 158,200 + 1,927` sum to `7,582,477`, but this aggregate match must **fail** row-level validation because multiple row values differ from the golden values.
- **Golden domestic rows:** `삼성전자 3,787,500`, `SK하이닉스 1,745,000`, `LS ELECTRIC 1,010,000`, `리노공업 597,600`, `대양전기공업 284,250`, `풍산 156,200`, `애니플러스 1,927` must be evaluated row-by-row before subtotal reconciliation.
- **Clean-room re-read:** when a previous answer is disputed, prior OCR values must not be reused as evidence before a fresh visual pass.
- **Patch-only ticker correction:** correcting `QQQ → QQQI` while retaining stale `19 shares / $9,738.01 / +$1,165.25 / +13.6%` must fail row atomicity against the golden `QQQI / 180 shares / $9,738.00 / +$149.56 / +1.5%`.
- **Current-pass verification:** a row claiming `VERIFIED` with only `identity` re-observed while quantity/value/P&L/return remain inherited must fail.
- **Summary clean-room coverage:** `valuation_date_text` is `9월 17일`; retaining prior `3월 17일(화)` after a re-read request must fail.

The repository golden fixture and scorer are:

- `tests/fixtures/financial_screenshot_118x2048_v1.json`
- `tests/evaluate_golden_fixture.py`
- `tests/test_evaluate_golden_fixture.py`

The fixture is an answer-key dataset only; the original screenshot is not bundled.

## 16. Response behavior

Apply the protocol silently unless methodology is requested. Return the requested result directly and state material source limitations when present.

Before delivery verify:

- [ ] no visual-inspection claim without inspected pixels;
- [ ] no invented detail from totals or recurring patterns;
- [ ] no displayed source value silently replaced by inference;
- [ ] every accessible source was covered before completion claims;
- [ ] proper nouns/identifiers obey Literal Identity Lock;
- [ ] confidence labels match visible evidence;
- [ ] every material structured row was validated independently before aggregate reconciliation;
- [ ] re-read/correction requests used a clean-room visual pass rather than patching prior output;
- [ ] any corrected/re-read row was re-observed atomically across every reported field;
- [ ] `VERIFIED` status reflects the current visual pass and was not inherited;
- [ ] a matching subtotal was not used to upgrade incorrect/uncertain rows;
- [ ] possible accidental cancellation was considered when row errors coexist with a matching subtotal;
- [ ] material arithmetic relationships were actually checked;
- [ ] no arithmetic mismatch was explained away without source evidence;
- [ ] validation is independent, not circular;
- [ ] structured outputs preserve field/row/column boundaries;
- [ ] completion status matches actual verified coverage and unresolved conflicts.
