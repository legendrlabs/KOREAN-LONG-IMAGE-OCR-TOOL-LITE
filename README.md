# KOREAN LONG IMAGE OCR TOOL LITE

> **AGENT SKILL / SKILL-ONLY PLUGIN PACKAGE — NOT AN OCR APPLICATION**
>
> 이 저장소는 OCR 실행 프로그램, API 래퍼, 이미지 슬라이서, 로컬 서버가 아닙니다. `GEMINI_API_KEY`, EasyOCR, Tesseract 또는 별도 OCR 스크립트를 요구하지 않습니다. 설치되는 호스트(ChatGPT/Codex/Gemini)가 제공하는 vision·file·connector 기능을 더 안전하고 일관되게 사용하도록 만드는 작업 프로토콜입니다.

한국어 장문 스크린샷·다중 이미지 OCR/복원 작업을 위한 경량 Agent Skill 배포판입니다.

**Current version: v0.1.1**

- [설치 가이드](./INSTALL.md)
- [v0.1.1 릴리스 노트](./RELEASE_NOTES_v0.1.1.md)
- [변경 이력](./CHANGELOG.md)
- [MIT License](./LICENSE)

## Quick install

### ChatGPT / Codex — GPT Lite

사전 패키징된 skill-only plugin ZIP:

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
```

지원되는 ChatGPT/Plugin 업로드 UI에서는 이 ZIP을 그대로 업로드할 수 있도록 `plugin.json`과 `skills/long-image-ocr-gpt-lite/SKILL.md`가 패키지 루트 기준으로 구성되어 있습니다.

ChatGPT Skills 업로드가 제공되는 계정이라면 canonical skill 폴더는 다음입니다.

```text
skills/long-image-ocr-gpt-lite/
```

### Gemini CLI — Gemini Lite

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

또는 패키지 파일:

```text
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

설치 후 실행 중인 Gemini CLI 세션에서는:

```text
/skills reload
```

## Included skills

| Variant | Canonical path | Focus |
|---|---|---|
| GPT Lite | `skills/long-image-ocr-gpt-lite/SKILL.md` | 짧은 배치 처리, 숫자 진행률, 체크포인트, 타임아웃/중단 후 재개 |
| Gemini Lite | `skills/long-image-ocr-gemini-lite/SKILL.md` | 원본 픽셀 우선, Drive/색인 텍스트 구분, 가짜 상세행 방지, 독립 검산 |

기존 v0.1.0 호환을 위해 루트의 `long-image-ocr-gpt-lite/`와 `long-image-ocr-gemini-lite/`도 당분간 유지합니다. 신규 설치는 `skills/` 경로를 권장합니다.

## Core guarantees

두 배포판 모두 다음 원칙을 공유합니다.

1. 원본 이미지 픽셀을 직접 확인하지 않았으면 시각 검증했다고 주장하지 않습니다.
2. 종목/행/항목 상세를 모르면 계좌 합계나 요약값으로 상세 데이터를 만들어내지 않습니다.
3. 화면에 표시된 수치와 계산·추정 수치를 구분합니다.
4. 일부만 검증한 결과를 전체 완료라고 표현하지 않습니다.
5. 집계값을 그대로 복사한 뒤 다시 비교하는 순환 검산을 인정하지 않습니다.

## GPT Lite

GPT 계열의 장시간 OCR 작업에서 다음을 강화합니다.

- 일반 이미지 5–10장, 긴 이미지 2–5장 단위 배치
- 배치별 숫자 진행률
- 증분 저장 및 체크포인트
- 타임아웃 후 첫 미검증 소스부터 재개
- `INTERRUPTED_RESUMABLE` 상태
- 백그라운드에서 계속 작업한다는 식의 허위 표현 금지

## Gemini Lite

Gemini 계열에서 Drive 색인 텍스트를 원본 이미지 판독으로 오인하거나, 현재 실행환경의 제한을 Google Drive 자체의 보편적 한계로 일반화하는 문제를 막기 위해 다음을 강화합니다.

- Source Access Gate
- `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE`
- 개별 파일 fetch/raw download/materialization 등 실제 원본 접근 경로 우선 확인
- `PORTFOLIO`, `TOTAL`, `OTHER HOLDINGS` 등 합계 기반 가짜 상세행 금지
- 화면 표시 P&L/수익률 우선 보존
- 독립 검산 및 완료 상태 게이트

## Portable plugin layout

```text
KOREAN-LONG-IMAGE-OCR-TOOL-LITE/
├─ plugin.json
├─ skills/
│  ├─ long-image-ocr-gpt-lite/
│  │  └─ SKILL.md
│  └─ long-image-ocr-gemini-lite/
│     └─ SKILL.md
├─ dist/
│  ├─ LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
│  └─ long-image-ocr-gemini-lite-v0.1.1.skill
├─ README.md
├─ INSTALL.md
├─ CHANGELOG.md
├─ LICENSE
├─ VERSION
├─ RELEASE_NOTES_v0.1.0.md
└─ RELEASE_NOTES_v0.1.1.md
```

The portable OpenAI plugin manifest is `plugin.json`. Portable plugin hosts discover skills from the root `skills/` directory.

## Status vocabulary

- `IN_PROGRESS`
- `COMPLETE_VERIFIED`
- `PARTIAL_VERIFIED`
- `INTERRUPTED_RESUMABLE`
- `DATA_HOLD`

## What this repository is not

이 저장소는 다음을 제공하지 않습니다.

- 자체 OCR 엔진
- Gemini/OpenAI API 호출 애플리케이션
- EasyOCR/Tesseract 설치 프로그램
- 이미지 자동 분할 실행기
- 백그라운드 서버

실제 이미지 접근, OCR/vision 성능, Drive 원본 접근 가능 여부는 설치되는 호스트와 그 호스트가 노출하는 도구 경로에 따라 달라집니다.

## Version

**v0.1.1 — Installable packaging update**

See [`CHANGELOG.md`](./CHANGELOG.md) and [`RELEASE_NOTES_v0.1.1.md`](./RELEASE_NOTES_v0.1.1.md).

## License

MIT — see [`LICENSE`](./LICENSE).
