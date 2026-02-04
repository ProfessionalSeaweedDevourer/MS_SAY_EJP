from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, ResultReason, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioConfig, AudioOutputConfig

sc = SpeechConfig(
    subscription="***REDACTED_AZURE_KEY***",
    region="eastus2"
)

aoc = AudioOutputConfig(True)
sc.speech_recognition_language = "ko-KR"

ac = AudioConfig(True) # 기본 마이크를 사용
sr = SpeechRecognizer(sc, ac)

print("음성 입력: ")
result = sr.recognize_once_async().get()

if result.reason == ResultReason.RecognizedSpeech:
    print(result.text)
elif result.reason == ResultReason.NoMatch:
    print(result.no_match_details)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)