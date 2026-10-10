# KOREAN LONG IMAGE OCR TOOL LITE

한국어 장문 스크린샷·다중 이미지 OCR/복원 작업을 위한 경량 Agent Skill 배포판입니다.

**Current version: v0.1.0**

- [설치 가이드](./INSTALL.md)
- [v0.1.0 릴리스 노트](./RELEASE_NOTES_v0.1.0.md)
- [변경 이력](./CHANGELOG.md)
- [MIT License](./LICENSE)

이 저장소는 같은 목적을 가진 두 개의 모델별 Lite 스킬을 제공합니다.

## Included skills

| Variant | Path | Focus |
|---|---|---|
| GPT Lite | `long-image-ocr-gpt-lite/SKILL.md` | 짧은 배치 처리, 숫자 진행률, 체크포인트, 타임아웃/중단 후 재개 |
| Gemini Lite | `long-image-ocr-gemini-lite/SKILL.md` | 원본 픽셀 우선, Drive/색인 텍스트 구분, 가짜 상세행 방지, 독립 검산 |

각 폴더는 독립 스킬입니다. 사용하는 호스트에 맞는 하위 폴더를 선택하는 것을 권장합니다.

## Core guarantees

두 배포판 모두 다음 원칙을 공유합니다.

1. 원본 이미지 픽셀을 직접 확인하지 않았으면 시각 검증했다고 주장하지 않습니다.
2. 종목/행/항목 상세를 모르면 계좌 합계나 요약값으로 상세 데이터를 만들어내지 않습니다.
3. 화면에 표시된 수치와 계산·추정 수치를 구분합니다.
4. 일부만 검증한 결과를 전체 완료라고 표현하지 않습니다.
5. 집계값을 그대로 복사한 뒤 다시 비교하는 순환 검산을 인정하지 않습니다.

## GPT Lite

GPT 계열에서 긴 OCR 작업이 타임아웃되거나 진행상태가 보이지 않는 문제를 줄이기 위해 다음을 추가로 강제합니다.

- 일반 이미지 5–10장, 긴 이미지 2–5장 단위 배치
- 배치별 숫자 진행률
- 증분 저장 및 체크포인트
- 타임아웃 후 첫 미검증 소스부터 재개
- `INTERRUPTED_RESUMABLE` 상태
- 백그라운드에서 계속 작업한다는 식의 허위 표현 금지

Skill path:

```text
long-image-ocr-gpt-lite/SKILL.md
```

## Gemini Lite

Gemini 계열에서 Drive 색인 텍스트를 원본 이미지 판독으로 오인하거나, 원본 접근 제한을 Google Drive 자체의 한계로 일반화하는 문제를 막기 위해 다음을 강화합니다.

- Source Access Gate
- `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE`
- 개별 파일 fetch/raw download/materialization 등 실제 원본 접근 경로 우선 확인
- `PORTFOLIO`, `TOTAL`, `OTHER HOLDINGS` 등 합계 기반 가짜 상세행 금지
- 화면 표시 P&L/수익률 우선 보존
- 독립 검산 및 완료 상태 게이트

Skill path:

```text
long-image-ocr-gemini-lite/SKILL.md
```

## Repository layout

```text
KOREAN-LONG-IMAGE-OCR-TOOL-LITE/
├─ README.md
├─ INSTALL.md
├─ CHANGELOG.md
├─ LICENSE
├─ VERSION
├─ RELEASE_NOTES_v0.1.0.md
├─ long-image-ocr-gpt-lite/
│  └─ SKILL.md
└─ long-image-ocr-gemini-lite/
   └─ SKILL.md
```

## Status vocabulary

스킬에 따라 다음 상태 중 필요한 항목을 사용합니다.

- `IN_PROGRESS`
- `COMPLETE_VERIFIED`
- `PARTIAL_VERIFIED`
- `INTERRUPTED_RESUMABLE`
- `DATA_HOLD`

## What this repository is not

이 저장소는 독립 실행형 OCR 엔진이나 특정 OCR 모델을 제공하지 않습니다.

목적은 모델이 이미지 기반 복원 작업을 수행할 때 다음을 강화하는 것입니다.

- 원본 충실도
- 검증 가능성
- 진행 가시성
- 중단 복구성
- 완료 상태의 정직한 표현

실제 이미지 접근, OCR 성능, 설치 방식은 사용하는 ChatGPT/Codex/Gemini 등의 호스트 환경과 제공 도구에 따라 달라집니다.

## Version

**v0.1.0 — Initial stable Lite distribution**

See [`CHANGELOG.md`](./CHANGELOG.md) and [`RELEASE_NOTES_v0.1.0.md`](./RELEASE_NOTES_v0.1.0.md) for details.

## License

MIT — see [`LICENSE`](./LICENSE).
