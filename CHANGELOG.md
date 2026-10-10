# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project uses semantic versioning where practical.

## [0.1.0] - 2026-10-11

### Added

- Initial dual-distribution Lite release.
- `long-image-ocr-gpt-lite` skill for bounded batch processing, numeric progress reporting, checkpointing, timeout recovery, and resumable OCR workflows.
- `long-image-ocr-gemini-lite` skill for source-modality enforcement, direct-pixel verification, Drive/indexed-text separation, independent validation, and anti-fabrication safeguards.
- `INSTALL.md` with ChatGPT, Codex, and Gemini installation guidance.
- MIT license.
- Explicit completion states including `COMPLETE_VERIFIED`, `PARTIAL_VERIFIED`, `INTERRUPTED_RESUMABLE`, and `DATA_HOLD`.
- Regression-oriented safeguards against synthetic aggregate rows such as `PORTFOLIO`, circular validation, and completion overstatement.

### Notes

This project provides model-execution guidance rather than an OCR engine. It is intended to improve source fidelity, progress visibility, and interruption resilience in image-based extraction and reconstruction tasks.
