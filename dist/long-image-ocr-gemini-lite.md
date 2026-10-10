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
Check source coverage, overlap duplicates, missing rows, numeric transcription, row/column shifts, literal identities, uncertainty, traceability, arithmetic consistency, aggregate reconciliation, and spreadsheet/formula errors when applicable.

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

## 9. Arithmetic Consistency Gate

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

## 10. Summary and independent validation

Recompute every summary, total, count, monthly rollup, or yearly rollup from the **final structured rows**.

Make explicit include/exclude decisions for overlap duplicates, cancellations/reversals, funding/top-ups, free/zero-value rows, and other non-counted evidence.

Valid:

`SUM(actual extracted detail) ↔ displayed source subtotal`

Invalid circular validation:

copy displayed subtotal → synthetic row → sum same row → compare to original subtotal → declare success.

Zero difference does not prove correctness when validation is circular.

## 11. Operating modes

### Auto
Default. Apply the full protocol for long, dense, repetitive, tabular, financial, or precision-sensitive sources.

### Exact transcription
Preserve visible wording/order. Do not silently autocorrect, normalize, or summarize unless asked. Apply Literal Identity Lock. Mark uncertainty explicitly.

### Structured extraction
Verify every row independently, preserve associations, never move values between rows, never create missing rows, preserve genuine duplicates, and normalize only when requested.

## 12. Completion gate

Final status must be exactly one of:

- `COMPLETE_VERIFIED`
- `PARTIAL_VERIFIED`
- `DATA_HOLD`

`COMPLETE_VERIFIED`: every source required for the requested result was verified at the necessary level, with no unresolved material arithmetic or identity conflicts.

`PARTIAL_VERIFIED`: some requested sources/details remain unverified or unrestored.

`DATA_HOLD`: access, ambiguity, arithmetic inconsistency, identity uncertainty, or validation failure makes the result unsafe to use.

When relevant, report:

- total sources
- `DIRECT_PIXEL_VERIFIED`
- `TEXT_INDEX_ONLY`
- `METADATA_ONLY`
- `UNAVAILABLE`
- detail complete / missing
- extracted rows/items
- unresolved ambiguities
- arithmetic mismatches still open

If status is not `COMPLETE_VERIFIED`, do not say complete, fully restored, fully verified, audit complete, all data reconstructed, or nothing missing.

## 13. Regression checks

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

## 14. Response behavior

Apply the protocol silently unless methodology is requested. Return the requested result directly and state material source limitations when present.

Before delivery verify:

- [ ] no visual-inspection claim without inspected pixels;
- [ ] no invented detail from totals or recurring patterns;
- [ ] no displayed source value silently replaced by inference;
- [ ] every accessible source was covered before completion claims;
- [ ] proper nouns/identifiers obey Literal Identity Lock;
- [ ] confidence labels match visible evidence;
- [ ] material arithmetic relationships were actually checked;
- [ ] no arithmetic mismatch was explained away without source evidence;
- [ ] validation is independent, not circular;
- [ ] structured outputs preserve field/row/column boundaries;
- [ ] completion status matches actual verified coverage and unresolved conflicts.
