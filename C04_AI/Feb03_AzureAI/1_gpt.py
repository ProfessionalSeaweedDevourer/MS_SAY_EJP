import os
from openai import AzureOpenAI

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1")
subscription_key = os.environ["AZURE_OPENAI_KEY"]
api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

msg = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    userInput = input("Q: ")
    if userInput.lower() in ["exit", "quit"]:
        break

    msg.append({"role": "user", "content": userInput})

    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=msg,
            extra_body={
                "data_sources": [
                    {
                        "type": "azure_search",
                        "parameters": {
                            "endpoint": "",  # search service > 개요 url
                            "index_name": "",  # 해당 검색 서비스에 지정한 인덱스 이름
                            "authentication": {
                                "type": "api_key",
                                "key": "",  # search service > 키
                            },
                            "embedding_dependency": {
                                "type": "api_key",
                                "key": "",  # 
                            },
                        },
                    }
                ]
            },
        )
        print(f"A: {response.choices[0].message.content}")
        msg.append(
            {"role": "assistant", "content": response.choices[0].message.content}
        )
    except Exception as e:
        print(f"\n[오류 발생]: {e}")
        break
