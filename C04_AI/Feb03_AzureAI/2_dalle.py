









while True:
    myMsg = input("Explain the image: ")
    if myMsg == 'exit':
        break
    result = client.images.generate(model="dall-e-3", prompt = myMsg)

    json_response = json.loads(result.model_dump_json())
    image_url = json_response["data"][0]["url"]

    f = open(f"C:/{myMsg}.png", "wb")
    f.write(requests.get(image_url).content)
    f.close()