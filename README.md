# 🧠 End-to-End MLOps for NLP

A complete MLOps pipeline for deploying a sentiment analysis application using modern DevOps tools and machine learning best practices. This project integrates data versioning, experiment tracking, containerization, orchestration, CI/CD automation, and real-time monitoring into a robust production-ready NLP workflow.

## 📌 Project Highlights

- 🔍 **Sentiment Analysis Model** with 95% accuracy
- 💾 **Version Control** for code, data, and models using Git, DVC, and MLflow
- 🐳 **Dockerized Microservice** for consistent deployment
- ☸️ **Kubernetes (EKS)** for scalable orchestration
- 🚀 **CI/CD** with GitHub Actions for automated deployment
- 📊 **Monitoring** using Prometheus and Grafana
- ☁️ **Cloud Infrastructure** on AWS (ECR, EKS, S3)

---


## ⚙️ Tech Stack

| Category         | Tools & Technologies                                |
|------------------|-----------------------------------------------------|
| **Language**     | Python                                              |
| **ML Framework** | Scikit-learn                                        |
| **Versioning**   | Git, DVC, MLflow, DagsHub                           |
| **CI/CD**        | GitHub Actions                                      |
| **Container**    | Docker                                              |
| **Cloud**        | AWS ECR, S3, EKS                                    |
| **Orchestration**| Kubernetes                                          |
| **Monitoring**   | Prometheus, Grafana                                 |

---

🚀 Quickstart
🔧 Setup Environment
```bash

git clone https://github.com/Samarth777415/End-to-End-MLOps-for-NLP.git
cd End-to-End-MLOps-for-NLP
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```
📦 Pull Data & Models via DVC
```bash
dvc pull
```
🧠 Train Model
```bash
python src/train.py
```
📊 Launch MLflow UI
```bash
mlflow ui
Access it at: http://localhost:5000
```
🐳 Docker Build & Run
```bash
docker build -t sentiment-app .
docker run -p 8000:8000 sentiment-app
```
☸️ Kubernetes Deployment (AWS EKS)
Update the ECR image name in kubernetes/deployment.yaml.

Apply the Kubernetes configurations:

```bash
kubectl apply -f kubernetes/
```
📈 Monitoring Setup
Prometheus and Grafana dashboards are integrated to monitor:

📍 Model latency

⏱️ API uptime

📊 Resource usage

Setup instructions are available in the monitoring/ directory.

📁 MLflow & DVC Example
🧪 All experiments are tracked using MLflow.

📦 Dataset and model versioning is handled via DVC and DagsHub.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

🌐 Live Demo / Deployment
Coming soon — hosted demo on AWS EKS cluster.


🙌 Acknowledgements
DagsHub

MLflow

Scikit-learn

Docker

Prometheus

Grafana
