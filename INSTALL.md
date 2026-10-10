# Installation Guide / 설치 가이드

> 이 저장소는 **Agent Skill / skill-only plugin 배포판**입니다. OCR 실행 프로그램이 아니며 `GEMINI_API_KEY`, EasyOCR, Tesseract, 별도 서버 또는 이미지 분할 스크립트를 설치할 필요가 없습니다.

Repository:

`https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

Current version: **v0.1.2**

---

# 1. 가장 먼저 고를 것

| 사용 환경 | 설치 대상 | 권장 방식 |
|---|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` | 기존 v0.1.1 Plugin/Skill 설치 |
| ChatGPT Desktop / Codex | `korean-long-image-ocr-tool-lite` plugin 또는 `long-image-ocr-gpt-lite` skill | 기존 v0.1.1 marketplace/plugin |
| Gemini 계열 | `long-image-ocr-gemini-lite` | **단일 Markdown 직접 등록 우선** |
| Gemini CLI | `long-image-ocr-gemini-lite` | Markdown 직접 등록 또는 Git/`.skill` fallback |

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

# 2. Gemini — Markdown 직접 등록을 최우선으로 사용

v0.1.2부터 Gemini 설치는 가능한 경우 **단일 Markdown 파일을 스킬로 직접 등록하는 방식**을 우선합니다.

배포 파일:

```text
dist/long-image-ocr-gemini-lite.md
```

이 파일은 canonical Gemini skill의 `SKILL.md`와 동일한 내용을 담습니다.

현재 환경에 다음과 같은 기능이 하나라도 있으면 이 경로를 먼저 사용합니다.

- Agent Skill 생성
- `SKILL.md` 업로드
- Markdown에서 Skill 생성
- 사용자/워크스페이스 Skill 등록
- 로컬 Skill directory에 Markdown 저장

등록 이름:

```text
long-image-ocr-gemini-lite
```

복붙용 요청문:

```text
dist/GEMINI_INSTALL_PROMPT.txt
```

내용의 핵심은 다음과 같습니다.

```text
이 Markdown 파일을 받아서 Agent Skill `long-image-ocr-gemini-lite`로 등록해줘.
현재 환경이 Markdown/SKILL.md 직접 등록을 지원하면 그 경로를 최우선으로 사용하고,
영구 스킬 등록 기능이 없으면 현재 대화에 지침만 로드 가능한 상태라고 정확히 알려줘.
이 저장소를 실행형 OCR 앱으로 해석하지 말고 npm/pip/GEMINI_API_KEY/별도 서버 같은
존재하지 않는 설치 절차를 만들지 마.
```

## 영구 설치와 현재 대화 로드는 다름

호스트가 Markdown 파일을 읽을 수 있다고 해서 반드시 계정/워크스페이스에 영구 Skill을 만들 수 있는 것은 아닙니다.

- **영구 Skill registry가 있음** → `long-image-ocr-gemini-lite`로 등록
- **파일 읽기만 가능하고 Skill registry가 없음** → 현재 대화에 지침을 로드해 사용 가능하지만 영구 설치라고 표현하지 않음
- **Gemini CLI 사용 가능** → 아래 CLI fallback 사용

어떤 경우에도 이 저장소를 다음과 같이 재해석하면 안 됩니다.

- `npm install`이 필요한 앱
- `pip install -r requirements.txt`가 필요한 Python 프로젝트
- `GEMINI_API_KEY`를 요구하는 API 프로그램
- EasyOCR/Tesseract 서버
- 이미지 분할 실행기

그러한 구성요소는 이 배포판에 존재하지 않습니다.

---

# 3. Gemini CLI fallback

직접 Markdown 등록 경로가 없고 Gemini CLI skill 설치 기능을 사용할 수 있다면 GitHub skill directory를 설치합니다.

## 사용자 전체에 설치

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

## 현재 workspace에만 설치

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope workspace
```

## `.skill` 호환 패키지

기존 v0.1.1 패키지도 유지합니다.

```text
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

다운로드 후 지원 환경에서 설치할 수 있습니다.

## 설치 확인

```bash
gemini skills list
```

이미 Gemini CLI 대화 세션을 열어둔 상태에서 설치했다면:

```text
/skills reload
```

그 후:

```text
/skills list
```

에서 `long-image-ocr-gemini-lite`가 보이는지 확인합니다.

---

# 4. ChatGPT 웹 / 앱

GPT 쪽 설치 경로는 v0.1.1과 동일하게 유지합니다.

## A. Plugin ZIP 업로드가 가능한 환경

GPT Lite 전용 패키지:

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
```

ZIP 내부:

```text
plugin.json
skills/
└─ long-image-ocr-gpt-lite/
   └─ SKILL.md
```

## B. ChatGPT Skills → Upload from your computer

Canonical skill:

```text
skills/long-image-ocr-gpt-lite/
```

핵심 파일:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
```

## C. Plugin Creator

`skills/long-image-ocr-gpt-lite/SKILL.md`를 전달해 skill-only plugin으로 등록합니다.

---

# 5. ChatGPT Desktop / Codex — GitHub marketplace

Repo marketplace:

```text
.agents/plugins/marketplace.json
```

Codex CLI:

```bash
codex plugin marketplace add legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE --ref main
codex plugin marketplace list
```

지원 환경에서 **Legendr Labs OCR Tools** source의:

```text
korean-long-image-ocr-tool-lite
```

를 설치합니다.

GPT OCR 작업에는 `long-image-ocr-gpt-lite`가 선택되어야 합니다.

---

# 6. 설치 후 테스트

## Gemini Lite 테스트

```text
이 Drive 폴더의 이미지들을 원본 기준으로 읽어서 상세 데이터를 복원해줘.
색인 텍스트와 실제 이미지 픽셀 확인 여부를 구분하고,
원본을 직접 보지 못한 항목은 미복원으로 남겨줘.
```

기대 동작:

- 원본 픽셀 접근 경로 우선 확인
- `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE` 구분
- `PORTFOLIO` 같은 합계 기반 가짜 상세행 금지
- 화면 표시값 우선 보존
- 부분 검증을 전체 완료라고 표현하지 않음
- 실행환경 제한을 Google Drive 자체의 보편적 한계로 일반화하지 않음

## GPT Lite 테스트

```text
이 스크린샷 여러 장을 날짜 순서대로 읽어서 표로 복원해줘.
긴 작업이면 작은 배치로 나누고, 배치마다 숫자 진행률과 체크포인트를 알려줘.
원본에서 확인되지 않은 상세값은 추정하지 마.
```

---

# 7. 스킬 설치가 새로 만들어주지 않는 기능

스킬 설치 자체가 다음 기능을 새로 추가하는 것은 아닙니다.

- Drive 원본 파일 접근 권한
- 모델 vision 기능
- OCR 엔진
- 인터넷/connector 접근 권한
- 백그라운드 실행 기능

스킬은 **호스트에 이미 존재하는 기능을 어떻게 사용하고, 실패·중단·검산을 어떻게 처리할지를 정의**합니다.

따라서 Drive 이미지 픽셀이 현재 호스트의 connector 경로에서 직접 노출되지 않는 경우, 스킬은 그 사실을 정확히 표시하고 가능한 원본 접근 경로를 점검하도록 강제하지만 존재하지 않는 도구 권한을 새로 만들어내지는 않습니다.

---

# 8. 업데이트

- **Gemini Markdown direct install**: 새 `dist/long-image-ocr-gemini-lite.md`로 기존 Skill 내용을 교체합니다.
- **Gemini CLI**: Git skill을 재설치/업데이트 후 `/skills reload`를 실행합니다.
- **ChatGPT Plugin ZIP / Skill**: 기존 v0.1.1 설치 흐름을 유지합니다.
- **Codex marketplace**: 기존 marketplace 갱신 절차를 사용합니다.

---

# 9. Compatibility note

v0.1.x 호환을 위해 다음 경로와 패키지는 유지합니다.

```text
long-image-ocr-gpt-lite/
long-image-ocr-gemini-lite/
skills/long-image-ocr-gpt-lite/
skills/long-image-ocr-gemini-lite/
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

Gemini 신규 설치의 가장 단순한 배포 파일은 다음입니다.

```text
dist/long-image-ocr-gemini-lite.md
```
