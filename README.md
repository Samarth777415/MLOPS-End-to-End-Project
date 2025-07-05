### 🧠 End-to-End MLOps for NLP

This project demonstrates a complete MLOps pipeline for an NLP-based sentiment analysis application. From model development and versioning to containerized deployment and monitoring, this repository showcases best practices for scalable and reproducible machine learning in production.

## 🚀 Project Overview

- **Task**: Sentiment Analysis (Binary Classification)
- **Objective**: Build, deploy, and monitor an NLP model using end-to-end MLOps workflows.
- **Accuracy**: Achieved 95% on validation data

## 🧩 Key Features

- ✅ **Model Training & Evaluation** with Scikit-learn
- 📦 **Data & Model Versioning** using Git, DVC, and MLflow (via DagsHub)
- 🐳 **Containerization** with Docker for consistent builds
- ☸️ **Orchestration** with Kubernetes on AWS EKS
- 🛠 **Deployment** using AWS ECR and CI/CD with GitHub Actions
- 📊 **Monitoring** with Prometheus and Grafana
- ☁️ **Cloud Storage** via AWS S3

## 🧪 Tech Stack

| Category         | Tools & Technologies                                |
|------------------|-----------------------------------------------------|
| Language         | Python                                              |
| ML Framework     | Scikit-learn                                        |
| Versioning       | Git, DVC, MLflow, DagsHub                           |
| Containerization | Docker                                              |
| CI/CD            | GitHub Actions                                      |
| Orchestration    | Kubernetes (AWS EKS)                                |
| Deployment       | AWS ECR, AWS S3                                     |
| Monitoring       | Prometheus, Grafana                                 |

## 📂 Repository Structure

.
├── data/ # Raw and processed datasets (tracked by DVC)
├── src/ # Source code (training, preprocessing, utils)
├── models/ # Saved models (versioned with MLflow)
├── docker/ # Dockerfiles and scripts for containerization
├── kubernetes/ # Deployment configs for EKS
├── monitoring/ # Prometheus and Grafana setup
├── .github/workflows/ # CI/CD pipelines (GitHub Actions)
├── dvc.yaml # DVC pipeline definition
├── mlflow_tracking/ # MLflow setup and experiments
└── README.md # Project documentation

pgsql
Copy
Edit

## 🔧 Setup & Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/End-to-End-MLOps-for-NLP.git
cd End-to-End-MLOps-for-NLP
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
3. Pull Data and Model using DVC
bash
Copy
Edit
dvc pull
4. Train the Model
bash
Copy
Edit
python src/train.py
5. Track with MLflow
bash
Copy
Edit
mlflow ui
🚢 Deployment
Docker Build
bash
Copy
Edit
docker build -t sentiment-app .
Push to AWS ECR and Deploy on EKS
See kubernetes/ folder for YAML configurations.

📈 Monitoring
Prometheus and Grafana are configured to track model performance and resource usage in real time.
Refer to monitoring/ directory for setup instructions.

📃 License
This project is licensed under the MIT License.

🤝 Acknowledgements
Inspired by best practices from the MLOps community

Thanks to open-source contributors and tool developers

