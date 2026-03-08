from PIL import Image
from fastapi import FastAPI,UploadFile,File
import uvicorn
from io import BytesIO
import numpy as np

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "Hello World"}

def read_file_as_image_data(data) -> np.ndarray:
    Image.open(BytesIO(data))
    pass

@app.post("/predict")
async def predict(
    file: UploadFile=File(...)
):
    bytes=read_file_as_image_data(await file.read())
    pass



if __name__ == "__main__":
    
    uvicorn.run(app, host="localhost", port=8000)