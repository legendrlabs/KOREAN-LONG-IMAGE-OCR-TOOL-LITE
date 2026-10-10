# v0.1.2 — Gemini Markdown-first install update

This update focuses only on Gemini installation ergonomics. GPT/ChatGPT Work packaging is unchanged because that path is already working in testing.

## Primary Gemini install artifact

Use the single Markdown file:

```text
dist/long-image-ocr-gemini-lite.md
```

This file is the Gemini Lite `SKILL.md` content distributed as a standalone Markdown artifact.

If the current host can create/register an Agent Skill from Markdown or `SKILL.md`, use this artifact first and register it as:

```text
long-image-ocr-gemini-lite
```

## Copy-paste installer prompt

A ready-to-use prompt is included at:

```text
dist/GEMINI_INSTALL_PROMPT.txt
```

It instructs the host to:

1. prefer direct Markdown/`SKILL.md` registration;
2. distinguish persistent installation from current-chat loading;
3. use Gemini CLI installation only as a fallback;
4. not invent `npm`, `pip`, `GEMINI_API_KEY`, local OCR servers, or executable app setup.

## Fallback paths

Gemini CLI Git install remains supported:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

The packaged `.skill` artifact from v0.1.1 is also retained for compatibility:

```text
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

## Important limitation

A host that can only read the Markdown as an attachment or web page, but exposes no persistent skill registry, may load the instructions for the current conversation but cannot honestly claim permanent installation.

This is a host capability limitation, not a reason to reinterpret this repository as an OCR application.
