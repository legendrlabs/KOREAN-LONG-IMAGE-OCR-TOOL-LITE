# Installation Guide / 설치 가이드

> 이 저장소는 **Agent Skill / skill-only plugin 배포판**입니다. OCR 실행 프로그램이 아니며 `GEMINI_API_KEY`, EasyOCR, Tesseract, 별도 서버 또는 이미지 분할 스크립트를 설치할 필요가 없습니다.

Repository:

`https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

Current repository version: **v0.1.4**

---

# 1. 설치 대상

| 환경 | 설치 대상 | 권장 방식 |
|---|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` | 기존 v0.1.1 Plugin/Skill 설치 |
| ChatGPT Desktop / Codex | GPT plugin 또는 `long-image-ocr-gpt-lite` | 기존 v0.1.1 marketplace/plugin |
| Gemini 계열 | `long-image-ocr-gemini-lite` | **단일 Markdown 직접 등록 우선** |
| Gemini CLI | `long-image-ocr-gemini-lite` | Markdown/Git/`.skill` 중 지원 경로 |

Canonical skill paths:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
skills/long-image-ocr-gemini-lite/SKILL.md
```

Gemini direct-distribution file:

```text
dist/long-image-ocr-gemini-lite.md
```

---

# 2. Gemini — Markdown 직접 등록 우선

Gemini 신규 설치에서는 가능한 경우 아래 단일 Markdown을 Agent Skill로 등록합니다.

```text
dist/long-image-ocr-gemini-lite.md
```

등록 이름:

```text
long-image-ocr-gemini-lite
```

이 파일은 canonical Gemini `SKILL.md`와 동일한 내용입니다.

복붙용 요청문:

```text
dist/GEMINI_INSTALL_PROMPT.txt
```

영구 Skill registry가 있으면 영구 등록하고, 파일 읽기만 가능하면 현재 대화에만 로드된 상태라고 정확히 표현해야 합니다.

어떤 경우에도 저장소를 `npm`, `pip`, `GEMINI_API_KEY`, EasyOCR/Tesseract 서버, MCP/Cloud Run OCR 서비스, 이미지 분할 실행기로 재해석하면 안 됩니다.

---

# 3. Gemini CLI fallback

사용자 전체:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

현재 workspace:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope workspace
```

현재 `.skill` package:

```text
dist/long-image-ocr-gemini-lite-v0.1.4.skill
```

설치 후 `/skills reload` 후 `/skills list`로 확인합니다.

---

# 4. Gemini v0.1.4 동작 확인

기본 테스트:

```text
이 이미지들을 원본 픽셀 기준으로 읽어 표로 복원해줘.
티커/회사명은 보이는 글자 그대로 적고, 익숙한 종목으로 자동 교정하지 마.
화면에 총자산·원금·손익처럼 산술적으로 연결된 값이 있으면 실제로 검산하고,
불일치하면 수수료나 반올림 탓으로 설명하지 말고 숫자를 재확인하거나 불확실하다고 표시해줘.
```

기대 동작:

- `QQQI → QQQ`, `GPIQ → UPRO`, `ROCQ → RDVY` 같은 의미 보정 금지
- 흐린 proper noun은 `AMBIGUOUS` / `UNREADABLE`
- `62,966,337 - 65,578,190 = -2,611,853` 같은 관계 실제 검산
- 산술 불일치 시 affected field를 verified 처리하지 않음
- 근거 없는 `fees`, `제비용`, `rounding`, FX, settlement 설명 금지
- confidence label은 실제 가독성에 맞춤
- 기존 source modality/coverage, 7-phase workflow, anti-fabrication, CSV/spreadsheet safety 유지

---

# 5. ChatGPT 웹 / 앱

GPT 쪽 설치물은 v0.1.4에서도 변경하지 않습니다.

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
skills/long-image-ocr-gpt-lite/SKILL.md
```

현재 ChatGPT Work 테스트 운용 중인 GPT skill 본문은 그대로 유지합니다.

---

# 6. ChatGPT Desktop / Codex marketplace

```bash
codex plugin marketplace add legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE --ref main
codex plugin marketplace list
```

지원 환경에서 **Legendr Labs OCR Tools** source의 `korean-long-image-ocr-tool-lite`를 설치합니다.

---

# 7. 이 스킬이 새로 만들어주지 않는 기능

스킬 설치 자체가 Drive 원본 접근 권한, 모델 vision 기능, OCR 엔진, 인터넷/connector 권한, 백그라운드 실행 기능을 새로 만들어주지는 않습니다.

스킬은 호스트에 이미 존재하는 기능을 어떻게 사용하고, 근거·누락·식별자·산술검산·완료 상태를 어떻게 관리할지 정의합니다.

---

# 8. 업데이트

- **Gemini Markdown direct install**: 새 `dist/long-image-ocr-gemini-lite.md`로 기존 Skill 내용을 교체
- **Gemini CLI Git install**: skill을 업데이트/재설치 후 `/skills reload`
- **Gemini `.skill`**: v0.1.4 package로 교체
- **GPT Plugin/Skill**: 현재 v0.1.1 설치 흐름 유지

---

# 9. Compatibility

이전 v0.1.x 경로/패키지는 기록과 호환을 위해 유지합니다. 신규 Gemini 설치는 다음 두 항목을 우선합니다.

```text
dist/long-image-ocr-gemini-lite.md
dist/long-image-ocr-gemini-lite-v0.1.4.skill
```
