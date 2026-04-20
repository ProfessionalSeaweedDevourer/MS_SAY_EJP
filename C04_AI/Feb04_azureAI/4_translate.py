import os

from azure.cognitiveservices.speech import SpeechRecognizer, ResultReason
from azure.cognitiveservices.speech.audio import AudioConfig
from azure.cognitiveservices.speech.translation import SpeechTranslationConfig, TranslationRecognizer
from pydash import result

stc = SpeechTranslationConfig(
    subscription=os.environ.get("AZURE_SPEECH_KEY"),
    region=os.environ.get("AZURE_SPEECH_REGION", "eastus2")
)
stc.speech_recognition_language = "ko-KR"
stc.add_target_language("en")
stc.add_target_language("ja")
ac = AudioConfig(True)
tr = TranslationRecognizer(stc, audio_config=ac)

print("지금 말하는 내용이 영어로 번역됩니다.")
result = tr.recognize_once_async().get()

if result.reason == ResultReason.RecognizedSpeech:
    print(result.text)
    print(result.translations["en"])
    print(result.translations["ja"])
elif result.reason == ResultReason.NoMatch:
    print(result.no_match_details)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)