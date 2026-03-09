# Api/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

# ------------------- FastAPI app -------------------
app = FastAPI(title="Potato Disease Detection API")

# Enable CORS so frontend can access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- Model Loading -------------------
# Detect latest model version automatically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
models_folder = os.path.join(BASE_DIR, "models")

version_folders = [v for v in os.listdir(models_folder) if v.isdigit()]
if not version_folders:
    raise RuntimeError("No model versions found in models/ folder")

latest_version = str(max([int(v) for v in version_folders]))
MODEL_PATH = os.path.join(models_folder, latest_version, "potatoes.h5")

model = tf.keras.models.load_model(MODEL_PATH)

# Class names in order of model outputs
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# ------------------- Helper function -------------------
def preprocess(image_bytes):
    """Convert uploaded image to model input"""
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((256, 256))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)  # batch dimension
    return image

# ------------------- Routes -------------------
@app.get("/")
def home():
    return {"message": "Potato Disease Detection API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        img = preprocess(image_bytes)
    except Exception:
        return {"error": "Invalid image file"}

    # Predict
    prediction = model.predict(img)[0]

    # Get top-2 predictions
    top_indices = np.argsort(prediction)[::-1][:2]
    top_predictions = [
        {"class": CLASS_NAMES[i], "confidence": float(prediction[i])}
        for i in top_indices
    ]

    return {"predictions": top_predictions}

# ------------------- Run server directly -------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)