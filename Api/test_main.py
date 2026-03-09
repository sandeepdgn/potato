import requests

# URL of your FastAPI backend
URL = "http://127.0.0.1:8000/predict"

# Path to the test image
IMAGE_PATH = "C:/Users/sandeep/Downloads/archive/PlantVillage/Potato___Early_blight/f0cdbf74-8401-48d1-b1cc-94862e1a4452___RS_Early.B 7447.JPG" 

with open(IMAGE_PATH, "rb") as f:
    files = {"file": f}
    response = requests.post(URL, files=files)

if response.status_code == 200:
    print("Prediction response:")
    print(response.json())
else:
    print("Error:", response.status_code, response.text)