# v0.1.1 — Installable packaging update

This release changes the repository from a source-only skill collection into a distribution that is easier for supported hosts to install directly.

## What changed

### ChatGPT / Codex

A portable plugin manifest is now included at the repository root:

```text
plugin.json
```

The canonical GPT skill is available at:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
```

A prebuilt GPT-only plugin ZIP is included:

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
```

The ZIP contains `plugin.json` at archive root and the GPT Lite skill under `skills/`, so eligible ChatGPT plugin upload flows do not need manual repackaging.

A repo marketplace is also included:

```text
.agents/plugins/marketplace.json
```

Supported Codex/ChatGPT Desktop environments can add the repository as a marketplace source:

```bash
codex plugin marketplace add legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE --ref main
```

### Gemini CLI

The canonical Gemini skill is available at:

```text
skills/long-image-ocr-gemini-lite/SKILL.md
```

Install from GitHub:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

A packaged `.skill` artifact is also included:

```text
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

After installation in an already-running interactive Gemini CLI session, run:

```text
/skills reload
```

## Important clarification

This repository is an **Agent Skill / skill-only plugin distribution**.

It is **not**:

- an OCR executable
- an EasyOCR/Tesseract wrapper
- a Gemini API application
- an image-slicing program
- a local server

No `GEMINI_API_KEY` is required by the skill itself. The host supplies whatever vision, file, connector, or OCR capabilities are available in that environment.

## Compatibility

The original top-level directories remain in v0.1.1 for compatibility:

```text
long-image-ocr-gpt-lite/
long-image-ocr-gemini-lite/
```

New installations should use the canonical `skills/` paths or the prebuilt package artifacts.
