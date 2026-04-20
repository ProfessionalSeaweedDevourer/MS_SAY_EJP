# pip install azure-ai-textanalytics==5.2.0

import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = os.environ.get("AZURE_LANGUAGE_KEY")
endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")

tac = TextAnalyticsClient(endpoint, AzureKeyCredential(key))

# ========================================================================================

InputTxt1 = ["야옹", "meow", "Ouf"] # Korean, English, French
# Language Detection

# for l in tac.detect_language(InputTxt1):
#     print(l.primary_language.name)

# ========================================================================================

InputTxt2 = ["자기합리화를 위한 창작은 선전을 위한 것보다도 더 추악한 것이다."]
# key phrase 분석

# results = tac.extract_key_phrases(InputTxt2, language="ko")
# language를 지정해 주면 정확도가 올라감.
# 1차 시도: 자, 한, 보다도, 추
# 수정 후 2차 시도: 자기합리화, 창작, 선전
# for r in results:
#     for p in r.key_phrases:
#         print(p)

# ========================================================================================

InputTxt3 = ["아렌트는 무의미하게 반복되는 삶이 아니라 자발적으로 삶의 가치를 찾으려 노력하는 삶을 살아야 한다고 역설한 것이다. 아렌트는 이런 삶의 가치는 결국 정치적 행위를 통해 이뤄질 수 있다고 보았다. 아렌트가 말하는 정치는 타인과 관계맺고 소통하는 것 일체를 말한다. 결국 상호관계를 얼마나 잘 이루느냐가 중요하다는 이야기를 '인간에 조건'에 써놓은 것이다. 아렌트는 '인간의 조건'에서 구상하기 시작한 정치철학을 나치 전체주의 정권 하에서 아렌트 자신이 경험한 것과 연관시켜 발전시켜 나간다. '왜 사람들은 전체주의에 매몰되는가?'를 고민한 아렌트는 아돌프 아이히만 재판 과정을 지켜보고 나서 악의 평범성이란 개념을 생각하게 된다."]
# 엔티티 분석: 각 단어의 '속성' 레이블링.

# results = tac.recognize_entities(documents=InputTxt3, language="ko")
# for r in results:
#     for e in r.entities:
#         print(e)

# {'text': '아렌트', 'category': 'Person', 'subcategory': None, 'length': 3, 'offset': 0, 
# 'confidence_score': 0.99}
# {'text': '반', 'category': 'Quantity', 'subcategory': 'Number', 'length': 1, 'offset': 11, 'confidence_score': 0.8}
# {'text': '아렌트', 'category': 'Person', 'subcategory': None, 'length': 3, 'offset': 65, 'confidence_score': 0.99}
# {'text': '아렌트', 'category': 'Person', 'subcategory': None, 'length': 3, 'offset': 109, 'confidence_score': 0.98}
# {'text': '정치', 'category': 'Skill', 'subcategory': None, 'length': 2, 'offset': 118, 'confidence_score': 0.99}
# {'text': '소통', 'category': 'Skill', 'subcategory': None, 'length': 2, 'offset': 131, 'confidence_score': 0.75}
# {'text': '인간', 'category': 'PersonType', 'subcategory': None, 'length': 2, 'offset': 180, 'confidence_score': 0.76}
# {'text': '아렌트', 'category': 'Person', 'subcategory': None, 'length': 3, 'offset': 198, 'confidence_score': 0.99}
# {'text': '정치철학', 'category': 'Skill', 'subcategory': None, 'length': 4, 'offset': 223, 'confidence_score': 0.96}
# {'text': '나치', 'category': 'Organization', 'subcategory': None, 'length': 2, 'offset': 229, 'confidence_score': 0.61}
# {'text': '아렌트', 'category': 'Person', 'subcategory': None, 'length': 3, 'offset': 244, 'confidence_score': 0.98}
# {'text': '이 경', 'category': 'Quantity', 'subcategory': 'Number', 'length': 3, 'offset': 250, 'confidence_score': 0.8}
# {'text': '사람들', 'category': 'PersonType', 'subcategory': None, 'length': 3, 'offset': 277, 'confidence_score': 0.71}
# {'text': '아렌트', 'category': 'Person', 'subcategory': None, 'length': 3, 'offset': 301, 'confidence_score': 0.98}
# {'text': '아돌프 아이히만', 'category': 'Person', 'subcategory': None, 'length': 8, 'offset': 306, 'confidence_score': 0.83}

# ========================================================================================

InputTxt4 = ["내가 당신을 사랑한 것은 당신이 뛰어나기 때문이고, 당신이 재능과 시정을 지니고 있기 때문이고, 당신이 위대한 시인의 꿈을 실현시키고 예술이라는 환영에 형태와 실체를 부여했기 때문이라고. 그런데 당신은 이 모든 것을 다 버리고 말았어... 당신의 예술이 없으면 당신은 아무것도 아니야."]
# 감정 분석

# results = tac.analyze_sentiment(documents=InputTxt4, language="ko")
# for r in results:
#     print(f"전체: {r.sentiment}")
#     print("긍정", r.confidence_scores.positive)
#     print("중립", r.confidence_scores.neutral)
#     print("부정", r.confidence_scores.negative)
#     print("-----")
#     for s in r.sentences:
#         print(s.text)
#         print(s.sentiment)
#         print("긍정", s.confidence_scores.positive)
#         print("중립", s.confidence_scores.neutral)
#         print("부정", s.confidence_scores.negative)
#         print("-----")

# 전체: positive
# 긍정 1.0
# 중립 0.0
# 부정 0.0
# -----
# 내가 당신을 사랑한 것은 당신이 뛰어나기 때문이고, 당신이 재능과 시정을 지니고 있기 때문 
# 이고, 당신이 위대한 시인의 꿈을 실현시키고 예술이라는 환영에 형태와 실체를 부여했기 때문
# 이라고.
# positive
# 긍정 1.0
# 중립 0.0
# 부정 0.0
# -----
# 그런데 당신은 이 모든 것을 다 버리고 말았어...
# neutral
# 긍정 0.0
# 중립 0.95
# 부정 0.05
# -----
# 당신의 예술이 없으면 당신은 아무것도 아니야.
# neutral
# 긍정 0.03
# 중립 0.66
# 부정 0.31

# ========================================================================================

InputTxt5 = ["환자는 3일 전부터 시작된 급성 인후통과 38.5도의 고열을 주소소견으로 내원함. 과거력상 제2형 당뇨로 인해 메트포르민을 복용 중임. 청진 시 수포음이 확인되어 흉부 X-선 검사를 시행한 결과 우측 하엽 폐렴이 의심됨. 이에 아목시실린 500mg을 1일 3회, 7일간 처방함."]

results = tac.begin_analyze_healthcare_entities(documents=InputTxt5)
for r in results.result():
    for e in r.entities:
        print("===")
        print(f"Entity: {e.text} / {e.normalized_text}") 
        print(f"Category: {e.category}")
        print(f"Subcategory: {e.subcategory}")
        print("===")

# ===
# Entity: 3일 전부터 / None
# Category: Time
# Subcategory: None
# ===
# ===
# Entity: 급성 / None
# Category: ConditionQualifier
# Subcategory: None
# ===
# ===
# Entity: 인후통과 / None
# Category: SymptomOrSign
# Subcategory: None
# ===
# ===
# Entity: 38.5도의 / None
# Category: MeasurementValue
# Subcategory: None
# ===
# ===
# Entity: 고열을 / None
# Category: SymptomOrSign
# Subcategory: None
# ===
# ===
# Entity: 내원함 / None
# Category: ConditionQualifier
# Subcategory: None
# ===
# ===
# Entity: 제2형 당뇨로 / None
# Category: Diagnosis
# Subcategory: None
# ===
# ===
# Entity: 메트포르민을 / None
# Category: MedicationName
# Subcategory: None
# ===
# ===
# Entity: 청진 / None
# Category: SymptomOrSign
# Subcategory: None
# ===
# ===
# Entity: 수포음이 / None
# Category: SymptomOrSign
# Subcategory: None
# ===
# ===
# Entity: 흉부 X-선 검사를 / None
# Category: ExaminationName
# Subcategory: None
# ===
# ===
# Entity: 우측 / None
# Category: Direction
# Subcategory: None
# ===
# ===
# Entity: 하엽 / None
# Category: BodyStructure
# Subcategory: None
# ===
# ===
# Entity: 폐렴이 / None
# Category: Diagnosis
# Subcategory: None
# ===
# ===
# Entity: 아목시실린 / None
# Category: MedicationName
# Subcategory: None
# ===
# ===
# Entity: 500mg을 / None
# Category: Dosage
# Subcategory: None
# ===
# ===
# Entity: 1일 / None
# Category: Frequency
# Subcategory: None
# ===
# ===
# Entity: 3회 / None
# Category: Frequency
# Subcategory: None
# ===
# ===
# Entity: 7일간 / None
# Category: Time
# Subcategory: None
# ===

# ============================