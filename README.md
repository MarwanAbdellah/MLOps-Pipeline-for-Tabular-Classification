# 🧪 MLOps Pipeline for Tabular Classification

An end-to-end **MLOps** pipeline project for classifying tabular data using **Scikit-learn**, **Docker**, **ONNX**, and **GitHub Actions**.

---

> Note: Explore the pipeline structure and how model training, evaluation, and deployment are automated.

**URL** = [https://github.com/MarwanAbdellah/MLOps-Pipeline-for-Tabular-Classification](https://github.com/MarwanAbdellah/MLOps-Pipeline-for-Tabular-Classification)

---

## 🧠 Overview

This project demonstrates a full MLOps workflow for tabular data classification — including preprocessing, model training, Docker containerization, CI/CD with GitHub Actions, and model export to **ONNX** format for deployment.

---

## 📁 Project Structure

```
MLOps-Pipeline-for-Tabular-Classification/
├── data/
│   └── Train.csv
├── Notebooks/
│   └── Train_classification.ipynb
├── notebooks/
│   └── model.onnx
├── .github/
│   └── workflows/
│       └── main.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Key Features

- 📊 Tabular classification using **Scikit-learn**
- 🔄 Model export to **ONNX** format
- 🐳 Pipeline orchestration with **Docker**
- ⚙️ Automated CI/CD using **GitHub Actions**
- ✅ Lightweight and modular project layout

---

## 🛠 Installation

### 1. Clone the Repository

```
git clone https://github.com/MarwanAbdellah/MLOps-Pipeline-for-Tabular-Classification.git
cd MLOps-Pipeline-for-Tabular-Classification
```

### 2. Create and Activate a Virtual Environment

```
python -m venv venv
```

- **Windows**: `venv\Scripts\activate`  
- **macOS/Linux**: `source venv/bin/activate`

### 3. Install Requirements

```
pip install -r requirements.txt
```

---

## 🐳 Build & Run with Docker

### Build the Docker image

```
docker build -t mlops_image .
```

### Run the container

```
docker run -di -p 8000:8000 --name mlops_image mlops_container
```

---

## 📦 Requirements

```
scikit-learn  
pandas  
numpy  
onnx  
onnxruntime  
pytorch  
matplotlib  
seaborn
```

Install using:

```
pip install -r requirements.txt
```

---

## 📌 .gitignore Suggestions

```
__pycache__/  
models/  
.venv/  
data/  
*.log  
```

---

## 📬 Contact

**Marwan Abdellah**  
📧 [marawan.abdellah0@gmail.com](mailto:marawan.abdellah0@gmail.com)  
🔗 GitHub: [@MarwanAbdellah](https://github.com/MarwanAbdellah)
