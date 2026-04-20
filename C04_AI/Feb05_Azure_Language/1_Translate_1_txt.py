import os

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

key = os.environ.get("AZURE_TRANSLATOR_KEY")
endpoint = os.environ.get("AZURE_TRANSLATOR_ENDPOINT", "https://api.cognitive.microsofttranslator.com/")
region = os.environ.get("AZURE_TRANSLATOR_REGION", "eastus2")

tc = TranslatorCredential(key, region) # 인증 먼저
ttc = TextTranslationClient(tc, ) # 인증 정보를 사용해 클라이언트 접속

targetLang = ["en", "ja", "de", "it", "fr", "tr", "el", "ard"]
# https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support 에서 대상 언어 확인 가능.
# 클링온어도 있음

txt = input("번역할 한국어 텍스트를 입력하십시오: ")
UserInput = [InputTextItem(text = txt)]

res = ttc.translate(content = UserInput, to = targetLang)
print(res)

# 1차 시도
# 번역할 한국어 텍스트를 입력하십시오: 위선도 선이라고 주장하고자 하는 자는 그 실패의 대가를 책임져야 한다.
# [{'detectedLanguage': {'language': 'ko', 'score': 1.0}, 'translations': [{'text': 'Those who want to claim that hypocrisy is also good must bear the price of their failure.', 'to': 'en'}, {'text': '偽
# 善も善だと主張したい者は、その失敗の代償を負わなければなりません。', 'to': 'ja'}, {'text': 'Degenen 
# die willen beweren dat hypocrisie ook goed is, moeten de prijs van hun falen dragen.', 'to': 'nl'}, 
# {'text': 'Ceux qui veulent prétendre que l’hypocrisie est aussi bonne doivent assumer le prix de leur échec.', 'to': 'fr'}, {'text': "QaQ je nejwI' 'e' maq neHchugh vay', QapHa'ghachchaj 'e' SIQnIS.", 'to': 'tlh-Latn'}, {'text': 'İkiyüzlülüğün de iyi olduğunu iddia etmek isteyenler, başarısızlığının bedelini katlanmak zorunda.', 'to': 'tr'}, {'text': "Chi vuole sostenere che anche l'ipocrisia sia
# buona deve pagare il prezzo del proprio fallimento.", 'to': 'it'}, {'text': 'Όσοι θέλουν να ισχυριστούν ότι η υποκρισία είναι επίσης καλή πρέπει να υποστούν το τίμημα της αποτυχίας τους.', 'to': 'el'}]}]

# 2차 시도
# 번역할 한국어 텍스트를 입력하십시오: 약자가 패배하는 사회는 야만적인 것으로, 이는 강자에 대한 복종이
#  아니라 불합리에 대한 복종이다. 
# [{'detectedLanguage': {'language': 'ko', 'score': 1.0}, 'translations': [{'text': 'A society in which the weak are defeated is barbaric, which is not submission to the strong, but submission to the unreasonable.', 'to': 'en'}, {'text': '弱者が敗北する社会は野蛮であり、それは強者への服従ではなく、理 
# 不尽な者への服従です。', 'to': 'ja'}, {'text': 'Eine Gesellschaft, in der die Schwachen besiegt werden, ist barbarisch, was nicht Unterwerfung gegenüber den Starken, sondern Unterwerfung unter die Unvernünftigen bedeutet.', 'to': 'de'}, {'text': "Una società in cui i deboli sono sconfitti è barbara, il che non è sottomissione ai forti, ma sottomissione all'irragionevole.", 'to': 'it'}, {'text': 'Une société où les faibles sont vaincus est barbare, ce qui n’est pas une soumission aux forts, mais 
# une soumission aux déraisonnables.', 'to': 'fr'}, {'text': 'Zayıfların yenildiği bir toplum barbarlıktır; güçlüye boyun eğmek değil, mantıksıza boyun eğmek.', 'to': 'tr'}, {'text': 'Μια κοινωνία στην 
# οποία οι αδύναμοι ηττώνται είναι βάρβαρη, που δεν είναι υποταγή στους δυνατούς, αλλά υποταγή στο παράλογο.', 'to': 'el'}, {'text': 'المجتمع الذي يهزم فيه الضعفاء هو مجتمع همجي، وهو ليس خضوعا للقوي، بل خضوع لغير المعقولين.', 'to': 'ar'}]}]
