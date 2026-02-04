from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

key = "  "
endpoint = "https://name.cognitiveservices.azure.com/"
cvc = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))

imgURL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgS3j4tJa799bP3n-jD_ssRBxxVDyJ__h8cg&s"

res = cvc.read(imgURL, raw = True)
ol = res.headers["Operation-Location"]
oID = ol.split("/")[-1]

while True:
    result = cvc.get_read_result(oID)
    if result.status not in ["notStarted", "running"]:
        break
    sleep(1)

print(result)