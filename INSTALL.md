# Installation Guide / 설치 가이드

> 이 저장소는 **Agent Skill / skill-only plugin 배포판**입니다. OCR 실행 프로그램이 아니며 `GEMINI_API_KEY`, EasyOCR, Tesseract, 별도 서버 또는 이미지 분할 스크립트를 설치할 필요가 없습니다.

Repository:

`https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

Current version: **v0.1.1**

---

# 1. 가장 먼저 고를 것

| 사용 환경 | 설치 대상 |
|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` |
| Codex | `long-image-ocr-gpt-lite` |
| Gemini CLI | `long-image-ocr-gemini-lite` |

Canonical skill paths:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
skills/long-image-ocr-gemini-lite/SKILL.md
```

---

# 2. ChatGPT 웹 / 앱

ChatGPT에서 Skills/Plugins 설치 기능은 계정·플랜·워크스페이스 설정에 따라 보이지 않을 수 있습니다.

## A. Plugin ZIP 업로드가 가능한 환경 — 가장 간단

GPT Lite 전용으로 미리 패키징한 파일:

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
```

이 ZIP 내부는 다음 구조입니다.

```text
plugin.json
skills/
└─ long-image-ocr-gpt-lite/
   └─ SKILL.md
```

즉, 별도로 압축을 다시 만들거나 파일 위치를 바꿀 필요가 없습니다.

Plugin ZIP 업로드 기능이 제공되는 워크스페이스에서는 해당 ZIP을 그대로 업로드합니다.

설치 후 새 채팅에서 필요하면:

```text
@Long Image OCR GPT Lite 이 이미지들을 원본 기준으로 복원해줘.
```

처럼 호출합니다.

## B. ChatGPT Skills → Upload from your computer가 보이는 환경

다음 canonical skill을 사용합니다.

```text
skills/long-image-ocr-gpt-lite/
```

핵심 파일은:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
```

Skills 화면에서 **Create → Upload from your computer**를 사용해 해당 skill을 등록합니다.

## C. Plugin Creator를 사용하는 경우

`@plugin-creator` 대화에서 다음 파일을 전달합니다.

```text
skills/long-image-ocr-gpt-lite/SKILL.md
```

요청 예시:

```text
이 SKILL.md를 포함하는 skill-only plugin을 만들어줘.
이름은 Long Image OCR GPT Lite로 하고 외부 앱이나 MCP는 추가하지 마.
이 스킬은 다중 이미지 OCR/복원에서 원본 검증, 소배치 처리,
숫자 진행률, 체크포인트, 중단 복구를 강제하는 용도야.
```

## D. GitHub URL만 채팅에 붙여 넣는 경우

일반 ChatGPT 채팅에 GitHub URL을 붙이는 것만으로 **항상 계정에 영구 설치되는 것은 아닙니다**.

해당 채팅이 GitHub 내용을 읽을 수 있다면 현재 대화에서 지침을 로드해 사용할 수는 있지만, 새 채팅 자동 적용을 원하는 경우 Skills/Plugin 설치 기능을 사용해야 합니다.

---

# 3. Gemini CLI

Gemini CLI는 Git repository의 특정 skill directory를 직접 설치할 수 있습니다.

## 사용자 전체에 설치

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

## 현재 workspace에만 설치

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope workspace
```

## 단일 `.skill` 패키지로 설치

배포 파일:

```text
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

다운로드 후:

```bash
gemini skills install ./long-image-ocr-gemini-lite-v0.1.1.skill --scope user
```

또는 workspace 범위:

```bash
gemini skills install ./long-image-ocr-gemini-lite-v0.1.1.skill --scope workspace
```

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

## 개발용 로컬 링크

```bash
git clone https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git
cd KOREAN-LONG-IMAGE-OCR-TOOL-LITE

gemini skills link ./skills/long-image-ocr-gemini-lite --scope user
```

---

# 4. Codex

이 저장소는 portable plugin 규격에 맞춰 루트에 `plugin.json`과 `skills/` 디렉터리를 둡니다.

GPT Lite canonical directory:

```text
skills/long-image-ocr-gpt-lite/
```

Codex 환경에서 직접 skill directory 설치가 가능한 경우 다음 GitHub 경로를 지정합니다.

```text
https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE/tree/main/skills/long-image-ocr-gpt-lite
```

Repo-local skills를 사용하는 프로젝트에서는 필요에 따라 해당 폴더를 `.agents/skills/long-image-ocr-gpt-lite/` 아래에 복사하거나 연결할 수 있습니다.

---

# 5. 설치 후 테스트

## GPT Lite 테스트

```text
이 스크린샷 여러 장을 날짜 순서대로 읽어서 표로 복원해줘.
긴 작업이면 작은 배치로 나누고, 배치마다 숫자 진행률과 체크포인트를 알려줘.
원본에서 확인되지 않은 상세값은 추정하지 마.
```

기대 동작:

- 일반 이미지 5–10장 또는 긴 이미지 2–5장 단위 처리
- `20/70` 같은 숫자 진행률
- 완료 배치 체크포인트
- 타임아웃/중단 시 첫 미검증 소스부터 재개
- 합계값으로 가짜 상세행을 생성하지 않음

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

---

# 6. 이 배포판이 설치 후 하지 않는 것

스킬 설치 자체가 다음 기능을 새로 추가하는 것은 아닙니다.

- Drive 원본 파일 접근 권한
- 모델 vision 기능
- OCR 엔진
- 인터넷/connector 접근 권한
- 백그라운드 실행 기능

스킬은 **호스트에 이미 존재하는 기능을 어떻게 사용하고, 실패·중단·검산을 어떻게 처리할지를 정의**합니다.

따라서 Drive 이미지 픽셀이 현재 호스트의 connector 경로에서 직접 노출되지 않는 경우, 스킬은 그 사실을 정확히 표시하고 가능한 원본 접근 경로를 점검하도록 강제하지만, 존재하지 않는 도구 권한을 새로 만들어내지는 않습니다.

---

# 7. 업데이트

새 버전으로 갱신할 때:

- **ChatGPT Plugin ZIP**: 새 ZIP으로 기존 plugin을 업데이트/교체합니다.
- **ChatGPT Skill**: 새 canonical skill 폴더/파일로 업데이트합니다.
- **Gemini CLI**: 재설치 후 `/skills reload`를 실행합니다.
- **Codex**: 설치된 skill/plugin을 새 버전으로 교체하고 필요하면 세션을 다시 시작합니다.

---

# 8. 제거

## Gemini CLI

```bash
gemini skills uninstall long-image-ocr-gemini-lite
```

## ChatGPT

Plugins 또는 Skills 화면에서 설치된 항목을 제거합니다.

## Codex

사용 중인 skill/plugin installer의 제거 절차를 사용하거나 설치된 skill directory를 제거합니다.

---

# 9. Compatibility note

v0.1.0 사용자를 위해 다음 legacy 경로는 v0.1.x 동안 유지합니다.

```text
long-image-ocr-gpt-lite/
long-image-ocr-gemini-lite/
```

신규 설치에는 다음 canonical 경로를 사용하십시오.

```text
skills/long-image-ocr-gpt-lite/
skills/long-image-ocr-gemini-lite/
```
