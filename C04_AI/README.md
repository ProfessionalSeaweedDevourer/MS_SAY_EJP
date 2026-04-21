# Highlight — Azure AI Integration Suite (C04_AI / Feb03~05)

> **[🇰🇷 한국어](#-한국어)** · **[🇺🇸 English](#-english)**

본 폴더의 Feb03~05 3일치 실습은 Azure OpenAI 와 여러 Azure Cognitive / AI Services 를 SDK 수준에서 직접 호출하며, 과정 최종 산출물(Highlight)에 해당합니다. (1월분 딥러닝 실습 `Jan27~30` 은 [Module ⑤ — AI Theory](../modules/05/README.md) 에서 다룹니다.)

---

## 🇰🇷 한국어

### 🎯 학습 목표

- Azure OpenAI Chat Completions · DALL·E 이미지 생성을 실제 SDK 로 호출
- Cognitive Services (Vision · Speech · Translator) 와 Azure AI Language 를 개별 호출 → 연쇄 파이프라인으로 구성
- 환경변수 주입 · 리소스 분리 · 다국어·음성·문서 번역·헬스케어 개체추출까지 실무형 조합 경험

### 🗂 파일 구성

| 파일 | 서비스 / SDK | 기능 |
|---|---|---|
| [Feb03_AzureAI/1_gpt.py](Feb03_AzureAI/1_gpt.py) | Azure OpenAI (`openai.AzureOpenAI`) | Chat Completions + Azure AI Search (RAG) 대화 루프 |
| [Feb03_AzureAI/2_dalle.py](Feb03_AzureAI/2_dalle.py) | Azure OpenAI DALL·E 3 (`client.images.generate`) | 프롬프트 → 이미지 URL → 로컬 저장 |
| [Feb04_azureAI/1_azurevision_ocr_webimg.py](Feb04_azureAI/1_azurevision_ocr_webimg.py) | Computer Vision (`azure.cognitiveservices.vision.computervision`) | 웹 이미지 URL → Read API (OCR) → 결과 폴링 |
| [Feb04_azureAI/2_azurespeech_voicerecognition.py](Feb04_azureAI/2_azurespeech_voicerecognition.py) | Speech (`SpeechRecognizer`) | 마이크 입력 → STT (`ko-KR`) |
| [Feb04_azureAI/3_tts.py](Feb04_azureAI/3_tts.py) | Speech (`SpeechSynthesizer`) | 텍스트 → 음성 합성 (`ko-KR-HyunsuNeural`) |
| [Feb04_azureAI/4_translate.py](Feb04_azureAI/4_translate.py) | Speech Translation (`TranslationRecognizer`) | 음성(ko) → 다국어(en/ja) 실시간 번역 |
| [Feb05_Azure_Language/1_Translate_1_txt.py](Feb05_Azure_Language/1_Translate_1_txt.py) | Translator (`TextTranslationClient`) | 텍스트 → 8개 대상 언어 일괄 번역 |
| [Feb05_Azure_Language/1_Translate_2_file.py](Feb05_Azure_Language/1_Translate_2_file.py) | Translator Document (`SingleDocumentTranslationClient`) | `.xlsx` 문서 → 단일 언어 번역 파일 출력 |
| [Feb05_Azure_Language/2_Language_1_langdetect.py](Feb05_Azure_Language/2_Language_1_langdetect.py) | Language (`TextAnalyticsClient`) | 언어 감지 · 핵심구 추출 · 개체 · 감성 · **헬스케어 개체** |

### 🔁 재현 가이드

#### 1. Azure 리소스 생성 순서

1. **Azure OpenAI** 리소스 생성 → `gpt-4.1` (또는 `gpt-4o`) 배포 생성, (선택) DALL·E 3 배포 추가
2. **Computer Vision** (또는 Cognitive Services multi-service) 리소스 생성
3. **Speech** 리소스 생성 (리전은 DALL·E 가용 리전과 다를 수 있음 — 별도 확인)
4. **Translator** 리소스 생성 — 리전·리전 헤더 모두 필요
5. **Language** (Text Analytics) 리소스 생성 — `healthcare entities` 는 일부 리전 한정
6. (1_gpt.py 의 RAG 부분을 쓸 경우) **Azure AI Search** 리소스 + 인덱스 준비

#### 2. 환경변수 (`.env`)

저장소 루트 [.env.example](../.env.example) 을 `.env` 로 복사 후 아래 키를 채운다.

```
AZURE_OPENAI_KEY= / AZURE_OPENAI_ENDPOINT= / AZURE_OPENAI_DEPLOYMENT=gpt-4.1 / AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_SPEECH_KEY= / AZURE_SPEECH_REGION=eastus2
AZURE_TRANSLATOR_KEY= / AZURE_TRANSLATOR_ENDPOINT= / AZURE_TRANSLATOR_REGION= / AZURE_TRANSLATOR_DOCUMENT_ENDPOINT=
AZURE_LANGUAGE_KEY= / AZURE_LANGUAGE_ENDPOINT=
```

`1_azurevision_ocr_webimg.py` 는 `key`·`endpoint` 가 파일 내 플레이스홀더(`"  "`, `https://name.cognitiveservices.azure.com/`) 로 남아있어 **직접 치환 필요** — 본 실습은 환경변수로 미전환됨.

#### 3. Python 패키지

```
pip install openai azure-cognitiveservices-vision-computervision azure-cognitiveservices-speech \
            azure-ai-translation-text azure-ai-translation-document \
            azure-ai-textanalytics==5.2.0 msrest requests
```

#### 4. 실행 순서 (추천)

| 단계 | 파일 | 입력 | 예상 출력 |
|---|---|---|---|
| 1 | `Feb03/1_gpt.py` | 터미널에서 `Q: 질문` | `A: ...` 어시스턴트 응답. `exit`/`quit` 로 종료 |
| 2 | `Feb03/2_dalle.py` | 프롬프트 | `C:/{prompt}.png` 저장 (Windows 전제 경로 — 다른 OS 는 경로 수정 필요) |
| 3 | `Feb04/1_ocr` | 파일 내 `imgURL` | `ReadOperationResult` 객체 — `.analyze_result.read_results[*].lines` 접근 |
| 4 | `Feb04/2_stt` | 마이크 음성 | 인식된 한국어 텍스트 1건 |
| 5 | `Feb04/3_tts` | 터미널 텍스트 | 스피커로 `ko-KR-HyunsuNeural` 합성 재생 |
| 6 | `Feb04/4_translate` | 마이크 한국어 | 원문 + 영어 + 일본어 번역 (STT + MT 합성) |
| 7 | `Feb05/1_Translate_1_txt` | 한국어 입력 | 8개 언어(en/ja/de/it/fr/tr/el/ar) 번역 딕셔너리 리스트 |
| 8 | `Feb05/1_Translate_2_file` | `Questions.xlsx` | `Questions_IT.xlsx` (이탈리아어로 문서 번역) |
| 9 | `Feb05/2_Language_1_langdetect` | 파일 하단 `InputTxt5` (의료 문장) | 헬스케어 개체 추출 결과(증상/약물/용량/해부학) |

파일 내 주석에 실제 과거 실행 출력 샘플이 일부 남아 있습니다 (`1_Translate_1_txt.py` 하단).

### ⚠️ 주의

- 과정에서 쓰던 Azure 구독은 **2026-04-20 부로 동결/해제**되었습니다. 본 저장소의 키·엔드포인트는 전부 비워져 있으며, 재현하려면 본인 구독에서 리소스를 새로 생성해야 합니다.
- `Feb03/2_dalle.py` 는 학습 중 상단 import·client 초기화가 제거된 상태로 커밋되어 있어 **그대로는 실행되지 않습니다** (학습 원본 보존 의도). 재현 시 `1_gpt.py` 의 `AzureOpenAI` client 설정을 참고해 복원 필요.
- `Feb04/1_azurevision_ocr_webimg.py` 는 `from time import sleep` 이 빠져 있어 폴링 루프 실행 전 import 추가가 필요합니다.
- `Feb04/4_translate.py` 는 `add_target_language("en")` 로 영어만 추가되지만 `stc.add_target_language("ja")` 도 있어 두 언어 번역을 확인할 수 있습니다.

---

## 🇺🇸 English

### 🎯 Learning Objectives

- Call Azure OpenAI Chat Completions and DALL·E image generation directly via the SDK
- Invoke Cognitive Services (Vision · Speech · Translator) and Azure AI Language individually, then compose them into a pipeline
- Hands-on experience with env-var injection, resource separation, and real-world combinations — multilingual MT, speech translation, document translation, healthcare entity extraction

### 🗂 File Layout

| File | Service / SDK | Feature |
|---|---|---|
| [Feb03_AzureAI/1_gpt.py](Feb03_AzureAI/1_gpt.py) | Azure OpenAI (`openai.AzureOpenAI`) | Chat Completions + Azure AI Search (RAG) conversation loop |
| [Feb03_AzureAI/2_dalle.py](Feb03_AzureAI/2_dalle.py) | Azure OpenAI DALL·E 3 (`client.images.generate`) | Prompt → image URL → save locally |
| [Feb04_azureAI/1_azurevision_ocr_webimg.py](Feb04_azureAI/1_azurevision_ocr_webimg.py) | Computer Vision | Web image URL → Read API (OCR) → poll for result |
| [Feb04_azureAI/2_azurespeech_voicerecognition.py](Feb04_azureAI/2_azurespeech_voicerecognition.py) | Speech (`SpeechRecognizer`) | Mic → STT (`ko-KR`) |
| [Feb04_azureAI/3_tts.py](Feb04_azureAI/3_tts.py) | Speech (`SpeechSynthesizer`) | Text → speech (`ko-KR-HyunsuNeural`) |
| [Feb04_azureAI/4_translate.py](Feb04_azureAI/4_translate.py) | Speech Translation | Voice (ko) → real-time multi-target (en/ja) translation |
| [Feb05_Azure_Language/1_Translate_1_txt.py](Feb05_Azure_Language/1_Translate_1_txt.py) | Translator (`TextTranslationClient`) | Text → batch translation into 8 target languages |
| [Feb05_Azure_Language/1_Translate_2_file.py](Feb05_Azure_Language/1_Translate_2_file.py) | Translator Document | `.xlsx` → translated output file |
| [Feb05_Azure_Language/2_Language_1_langdetect.py](Feb05_Azure_Language/2_Language_1_langdetect.py) | Language (`TextAnalyticsClient`) | Language detect · key phrases · entities · sentiment · **healthcare entities** |

### 🔁 Reproduction Guide

#### 1. Provision Azure resources (in order)

1. **Azure OpenAI** resource → deploy `gpt-4.1` (or `gpt-4o`); optionally add a DALL·E 3 deployment
2. **Computer Vision** (or a multi-service Cognitive Services) resource
3. **Speech** resource (its available region may differ from DALL·E — verify separately)
4. **Translator** resource — both key and region are required
5. **Language** (Text Analytics) resource — `healthcare entities` is region-limited
6. (If using the RAG block in `1_gpt.py`) **Azure AI Search** resource + index

#### 2. Environment variables (`.env`)

Copy [.env.example](../.env.example) at the repo root to `.env` and fill in:

```
AZURE_OPENAI_KEY= / AZURE_OPENAI_ENDPOINT= / AZURE_OPENAI_DEPLOYMENT=gpt-4.1 / AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_SPEECH_KEY= / AZURE_SPEECH_REGION=eastus2
AZURE_TRANSLATOR_KEY= / AZURE_TRANSLATOR_ENDPOINT= / AZURE_TRANSLATOR_REGION= / AZURE_TRANSLATOR_DOCUMENT_ENDPOINT=
AZURE_LANGUAGE_KEY= / AZURE_LANGUAGE_ENDPOINT=
```

`1_azurevision_ocr_webimg.py` keeps `key` / `endpoint` as in-file placeholders (`"  "`, `https://name.cognitiveservices.azure.com/`) — **substitute directly**; this file was not migrated to env vars.

#### 3. Python packages

```
pip install openai azure-cognitiveservices-vision-computervision azure-cognitiveservices-speech \
            azure-ai-translation-text azure-ai-translation-document \
            azure-ai-textanalytics==5.2.0 msrest requests
```

#### 4. Recommended run order

| Step | File | Input | Expected output |
|---|---|---|---|
| 1 | `Feb03/1_gpt.py` | `Q: question` at the prompt | `A: ...` assistant reply. `exit` / `quit` to end |
| 2 | `Feb03/2_dalle.py` | Prompt | Saved to `C:/{prompt}.png` (Windows path — change on other OSes) |
| 3 | `Feb04/1_ocr` | `imgURL` in the file | `ReadOperationResult` — inspect `.analyze_result.read_results[*].lines` |
| 4 | `Feb04/2_stt` | Mic | Recognized Korean text (one utterance) |
| 5 | `Feb04/3_tts` | Typed text | `ko-KR-HyunsuNeural` synthesized speech to speaker |
| 6 | `Feb04/4_translate` | Korean mic input | Original + English + Japanese translation (STT + MT) |
| 7 | `Feb05/1_Translate_1_txt` | Korean input | List of translation dicts for 8 languages (en/ja/de/it/fr/tr/el/ar) |
| 8 | `Feb05/1_Translate_2_file` | `Questions.xlsx` | `Questions_IT.xlsx` (document translated to Italian) |
| 9 | `Feb05/2_Language_1_langdetect` | `InputTxt5` near the bottom (clinical sentence) | Healthcare entities (symptom / medication / dosage / anatomy) |

Some past-run outputs are preserved as comments (see the bottom of `1_Translate_1_txt.py`).

### ⚠️ Notes

- The Azure subscription used in class was **frozen / decommissioned on 2026-04-20**. Every key and endpoint in this repo is blank; reproduction requires new resources on your own subscription.
- `Feb03/2_dalle.py` was committed with its top-of-file imports and client initialization stripped out (preserved as-is from class), so **it will not run as-is**. Restore it by copying the `AzureOpenAI` client setup from `1_gpt.py`.
- `Feb04/1_azurevision_ocr_webimg.py` is missing `from time import sleep`; add the import before the polling loop.
- `Feb04/4_translate.py` calls both `stc.add_target_language("en")` and `stc.add_target_language("ja")`, so you will see both translations.
