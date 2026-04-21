# Module ⑥ — MS Azure AI (GPT · Vision · Speech · Translator)

> **[🇰🇷 한국어](#-한국어)** · **[🇺🇸 English](#-english)**

---

## 🇰🇷 한국어

과정의 최종 구간으로, Azure OpenAI(GPT/DALL·E) 와 Azure Cognitive Services(Vision · Speech · Translator · Language) 를 **실제 SDK 호출 수준**에서 다룹니다. AI-900 수료 직전 단계.

### 🗂 포함 디렉토리

| 경로 | 주제 |
|---|---|
| [../../C04_AI/Feb03_AzureAI/](../../C04_AI/Feb03_AzureAI/) | Azure OpenAI · Vision · Speech 기본 호출 |
| [../../C04_AI/Feb04_azureAI/](../../C04_AI/Feb04_azureAI/) | DALL·E · Translator · 복합 시나리오 |
| [../../C04_AI/Feb05_Azure_Language/](../../C04_AI/Feb05_Azure_Language/) | Azure AI Language — 감성 분석 · 개체 추출 등 |

### 🎯 핵심 학습 주제

- Azure OpenAI GPT 호출 (Chat Completions · 프롬프트 설계)
- DALL·E 이미지 생성 파이프라인
- Azure Vision — OCR · 이미지 분석
- Azure Speech — STT/TTS, 언어 자동 감지
- Azure Translator — 다국어 번역 (KO/EN/FR/IT/JP/NL 실습: 루트의 `Questions_*.xlsx` 참고)
- Azure AI Language — 감성/개체/PII

### ⭐ Highlight

**Azure AI Integration Suite** — 본 모듈 전체가 대표 산출물입니다. 여러 Cognitive Services 를 조합해 OCR → 번역 → 요약 → 감성 분석까지 이어지는 통합 흐름을 구성한 실습이 포함되어 있습니다.

### 🔁 재현 주의 (중요)

- **수업에서 사용한 Azure 구독은 교육 종료와 함께 동결**되어, 본 저장소의 Azure 호출 코드는 **그대로 실행되지 않습니다**.
- 본인 Azure 구독에서 Cognitive Services 리소스를 생성한 뒤:
  1. 저장소 루트의 [../../.env.example](../../.env.example) 을 `.env` 로 복사
  2. 각 서비스(Azure OpenAI · Vision · Speech · Translator · Language) 의 키·엔드포인트·리전을 주입
  3. `AZURE_SPEECH_REGION` 기본값 `eastus2` 는 본인 리전으로 교체
- 리소스 유형·리전에 따라 일부 모델(예: DALL·E) 은 별도 배포가 필요합니다.

---

## 🇺🇸 English

The final stretch of the program. This module uses **Azure OpenAI (GPT / DALL·E)** and **Azure Cognitive Services (Vision · Speech · Translator · Language)** at actual SDK-call depth. Immediately precedes the AI-900 certification.

### 🗂 Included Directories

| Path | Topic |
|---|---|
| [../../C04_AI/Feb03_AzureAI/](../../C04_AI/Feb03_AzureAI/) | Azure OpenAI · Vision · Speech basics |
| [../../C04_AI/Feb04_azureAI/](../../C04_AI/Feb04_azureAI/) | DALL·E · Translator · composite scenarios |
| [../../C04_AI/Feb05_Azure_Language/](../../C04_AI/Feb05_Azure_Language/) | Azure AI Language — sentiment · entity extraction |

### 🎯 Key Topics

- Azure OpenAI GPT calls (Chat Completions · prompt design)
- DALL·E image-generation pipeline
- Azure Vision — OCR · image analysis
- Azure Speech — STT/TTS, language auto-detect
- Azure Translator — multilingual translation (KO/EN/FR/IT/JP/NL exercises; see `Questions_*.xlsx` at the repo root)
- Azure AI Language — sentiment · entity · PII

### ⭐ Highlight

**Azure AI Integration Suite** — the entire module is the deliverable. It includes a composite flow chaining multiple Cognitive Services (OCR → translation → summarization → sentiment analysis).

### 🔁 Reproduction Notes (Important)

- **The Azure subscription used in class was decommissioned** when the program ended, so Azure-dependent code **will not run out of the box**.
- To reproduce on your own subscription:
  1. Copy [../../.env.example](../../.env.example) to `.env` at the repo root
  2. Fill in keys, endpoints, and regions for each service (Azure OpenAI · Vision · Speech · Translator · Language)
  3. Replace the default `AZURE_SPEECH_REGION=eastus2` with your own region
- Depending on resource type and region, some models (e.g., DALL·E) require separate deployment.
