import os
from argparse import FileType
from fileinput import filename
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import SingleDocumentTranslationClient
from azure.ai.translation.document.models import DocumentTranslateContent
from pydantic import FilePath

key = os.environ.get("AZURE_TRANSLATOR_KEY")
endpoint = os.environ.get("AZURE_TRANSLATOR_DOCUMENT_ENDPOINT")
# region = "eastus2"

sdtc = SingleDocumentTranslationClient(endpoint, AzureKeyCredential(key))

FilePath = "Questions.xlsx"
fileName = FilePath.split("/")[-1]
FileType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" 
# https://learn.microsoft.com/ko-kr/azure/ai-services/translator/document-translation/reference/get-supported-document-formats
# 위 링크에서 파일 유형별 contentTypes 확인 가능

f = open(FilePath, "rb") #read binary 모드
fileContent = f.read()

docContent = (fileName, fileContent, FileType) # tuple로 묶어야 입력 가능
dtc = DocumentTranslateContent(document=docContent)
result = sdtc.document_translate(body = dtc, target_language="it")

f2 = open("Questions_IT.xlsx", "wb")

f2.write(result)
f2.close()