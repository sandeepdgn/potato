# 🥔 Potato Leaf Disease Detection API

A Machine Learning powered system that detects **potato leaf diseases from images**.
The project trains a deep learning model to classify potato leaves and exposes the model through a **FastAPI backend** for real-time predictions.

The system identifies three classes:

* **Healthy**
* **Early Blight**
* **Late Blight**

This project demonstrates a full ML pipeline including **model training, API development, and local testing**.

---

# 📌 Project Overview

Potato crops are vulnerable to several diseases that significantly reduce yield and crop quality. Early detection can help farmers take preventive measures.

This project uses **image classification** to automatically detect diseases from potato leaf images.

Workflow:

1. Collect and prepare dataset
2. Train deep learning model
3. Save trained model
4. Deploy model with FastAPI
5. Predict disease from uploaded leaf images

---

# 🧠 Model Classes

| Class        | Description                                  |
| ------------ | -------------------------------------------- |
| Healthy      | Leaf without disease                         |
| Early Blight | Fungal disease caused by *Alternaria solani* |
| Late Blight  | Disease caused by *Phytophthora infestans*   |

---

# ⚙️ Tech Stack

* Python
* TensorFlow / Keras
* FastAPI
* NumPy
* OpenCV
* Matplotlib
* Uvicorn
* Jupyter Notebook

---

# 📁 Project Structure

```id="fy6yqe"
potato-leaf-disease-detection/
│
├── Api/
│   ├── main.py          # FastAPI application
│   └── test.py          # Script to test API responses
│
├── notebooks/
│   └── training.ipynb   # Model training notebook
│
├── models/              # Saved trained models
│
├── index.html           # Simple local demo page
│
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

# 🚀 Installation

### 1. Clone the repository

```id="g6rr1c"
git clone https://github.com/yourusername/potato_leaf.git
cd potato_leaf
```

### 2. Create a virtual environment

```id="g7dc8y"
python -m venv venv
```

### 3. Activate the environment

Windows:

```id="bdceo6"
venv\Scripts\activate
```

Linux / macOS:

```id="sfz55a"
source venv/bin/activate
```

### 4. Install dependencies

```id="p9j9u3"
pip install -r requirements.txt
```

---

# 🧠 Model Training

Before running the API, you must train the machine learning model.

The training process is implemented in the notebook:

```id="3cb5ld"
notebooks/training.ipynb
```

### Steps

1. Start Jupyter Notebook

```id="t2qsbq"
jupyter notebook
```

2. Open the notebook

```id="kqvgr8"
notebooks/training.ipynb
```

3. Run all cells to:

* Load dataset
* Preprocess images
* Train the model
* Evaluate performance
* Save the trained model

The trained model will be saved in:

```id="72m24b"
models/
```

Example:

```id="pxbz4c"
models/{model_version}/potato_disease_model.h5
```

---

# ▶️ Running the API

After training the model, start the FastAPI server:

```id="w14qkw"
uvicorn Api.main:app --reload
```

The API will run at:

```id="l3x6eq"
http://127.0.0.1:8000
```

Interactive API documentation:

```id="poafxc"
http://127.0.0.1:8000/docs
```

---

# 🧪 Testing the API

### Method 1: Using FastAPI Docs

Open:

```id="s0w4xf"
http://127.0.0.1:8000/docs
```

Upload an image and receive the predicted disease class.

### Method 2: Using the test script

```id="3s6h3h"
python Api/test.py
```

---

# 🌐 Local Demo

A simple HTML page (`index.html`) is included to demonstrate how the API works locally.
It allows users to upload an image and view the predicted disease response from the API.

---

# 📊 Dataset

This project uses the **PlantVillage Dataset** for training the potato leaf disease classification model.

Dataset source:

https://www.kaggle.com/datasets/arjuntejaswi/plant-village/data

### Dataset Credits

The dataset originates from the **PlantVillage Project**, which provides publicly available plant disease datasets for machine learning research in agriculture.

If you use this project for research or further development, please acknowledge the dataset creators.

---

# 🔮 Future Improvements

* Improve model accuracy
* Add disease severity detection
* Deploy the API to cloud
* Create a mobile application for farmers
* Real-time camera detection
* Support more plant diseases

---

# 👨‍💻 Author

**Sandeep**


---

