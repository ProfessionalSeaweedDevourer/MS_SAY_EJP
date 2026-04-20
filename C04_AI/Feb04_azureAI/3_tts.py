import os

from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, ResultReason, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from sqlalchemy import Result

sc = SpeechConfig(
    subscription=os.environ.get("AZURE_SPEECH_KEY"),
    region=os.environ.get("AZURE_SPEECH_REGION", "eastus2")
)
aoc = AudioOutputConfig(True)
sc.speech_synthesis_voice_name = "ko-KR-HyunsuNeural"
ss = SpeechSynthesizer(sc, aoc)

print("텍스트 입력: ", end=' ')
txt = input()

result = ss.speak_text_async(txt).get()

if result.reason == ResultReason.SynthesizingAudioCompleted:
    print(txt)
elif result.reason == ResultReason.Canceled:
    print(result.cancellation_details)