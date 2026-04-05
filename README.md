# 🧠 Agentic Quantum-Safe Privacy Framework (AQSPF)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pii-privacy-app.streamlit.app/)
[![Demo Drive](https://img.shields.io/badge/Demo-Google%20Drive-green?logo=google-drive)](https://drive.google.com/drive/folders/1TqMvqNkHZtyQxz7UKHxHSbr6f1Lqs0Dj)

An AI-powered privacy protection system that detects Personally Identifiable Information (PII) in text and images, then applies quantum-inspired privacy scoring and post-quantum cryptography (PQC) encryption.

## 🎥 Demo

Access the demo files and walkthrough here:  
👉 https://drive.google.com/drive/folders/1TqMvqNkHZtyQxz7UKHxHSbr6f1Lqs0Dj

## 🚀 Live Demo

**Try it now:** [https://pii-privacy-app.streamlit.app/](https://pii-privacy-app.streamlit.app/)

## 🏗️ AWS Pipeline Architecture

![AWS Pipeline Architecture](https://raw.githubusercontent.com/HaswanthVIT/pii-privacy-app/main/AWS-PII-Architecture-Diagram.png)

## Features

### 1️⃣ AI-Powered PII Detection
- **BERT-based Named Entity Recognition**
- Detects: Names, Locations, Organizations
- Regex detection:
  - Emails
  - Phone numbers
  - Spelled-out numbers
- Real-time confidence scoring

### 2️⃣ Image PII Detection
- OpenAI CLIP multimodal analysis
- Detects:
  - Credit cards
  - ID cards
  - Passports
  - Documents
- Visual similarity confidence scoring

### 3️⃣ Quantum Privacy Evaluation
- Combines text + image confidence
- Quantum-inspired privacy score
- Suggests anonymization strength

### 4️⃣ Post-Quantum Cryptography (PQC)
- Simulated Kyber-based encryption
- Hash-based key exchange
- XOR cipher with derived symmetric keys
- Base64 encoded encrypted payload

---

## ☁️ AWS Data Engineering Extension

In addition to the real-time AI application, this project demonstrates a production-grade AWS batch data pipeline for scalable privacy-focused data processing.

### 🏗️ AWS Pipeline Architecture
```
[ Streamlit App / External Sources ]
                ↓
      Amazon S3 (Raw Zone - JSON)
                ↓
    Amazon EC2 (PySpark ETL Engine)
                ↓
      Amazon S3 (Processed - Parquet)
                ↓
          Spark SQL Analytics
                ↓
      Amazon CloudWatch Monitoring
```

### 🗂️ 1. Data Lake Architecture (Amazon S3)
- **Raw Zone:** Stores incoming JSON data
- **Processed Zone:** Stores masked & validated Parquet files
- Structured lifecycle separation
- Schema validation layer

### ⚙️ 2. Batch ETL with PySpark on EC2
- Apache Spark configured on EC2
- ETL script: `spark_etl.py`

**ETL Responsibilities:**
- Read raw JSON from S3
- Validate schema
- Apply regex-based PII masking
- Add processing timestamps
- Write optimized Parquet output

**Execution:**
```bash
spark-submit spark_etl.py
```

### 🔐 3. Secure Infrastructure (IAM)
- EC2 instance role attached
- Least-privilege permissions
- No hardcoded AWS credentials
- S3 + CloudWatch access only

**IAM Policy Artifact:**
```
docs/aws-evidence/iam_role_policy.json
```

### 📊 4. Observability with CloudWatch
- ETL execution logs captured
- EC2 CPU monitoring
- Health tracking
- Audit-ready log streams

**Artifacts:**
```
docs/aws-evidence/etl_execution_cloudwatch.json
docs/aws-evidence/ec2_cpu_metrics.csv
```

### 📦 5. Processed Output & Metadata
- Parquet storage optimized for analytics
- Query-ready via Spark SQL

**Artifacts:**
```
docs/aws-evidence/processed_sample.csv
docs/aws-evidence/s3_processed_metadata.json
docs/aws-evidence/aws_data_pipeline_architecture.png
```

### 🔗 AWS Resources Used
- Amazon EC2
- Amazon S3
- Amazon CloudWatch
- AWS IAM
- Apache Spark (PySpark)

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| NLP Model | BERT (`dslim/bert-base-NER`) |
| Vision Model | CLIP (`openai/clip-vit-base-patch32`) |
| Framework | PyTorch, Transformers |
| Cryptography | Hashlib, Secrets (stdlib) |
| Cloud & Data | AWS EC2, S3, CloudWatch, IAM, PySpark |

---

## 📋 Requirements
```
transformers==4.57.1
torch>=2.0.0
torchvision
pillow
streamlit>=1.51.0
accelerate
sentencepiece
protobuf
```

---

## 💻 Local Installation
```bash
git clone https://github.com/yourusername/aqspf-privacy-app.git
cd aqspf-privacy-app

pip install -r requirements.txt
streamlit run app.py
```

App runs at: `http://localhost:8501`

---

## 🔬 Project Background

This project explores:
- AI-powered multimodal PII detection
- Quantum-inspired privacy scoring
- Post-quantum cryptography readiness
- Enterprise-grade AWS data engineering

| Stage | Platform |
|---|---|
| Original Development | Google Colab |
| Deployment | Streamlit Cloud |
| Infrastructure Extension | AWS |

---

## ⚠️ Limitations

- First load may take 1–2 minutes
- Streamlit free tier sleeps after inactivity
- PQC is simulated (educational purposes only)
- Not production-grade encryption

---

## 🔐 Privacy Notice

- No data stored
- No external transmission
- In-memory processing only
- Uploaded content is not saved

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue or submit a PR.

---

## 📝 License

[MIT License](LICENSE)

---

## 👨‍💻 Author

Developed with ❤️ for advancing privacy-preserving AI systems and secure cloud data engineering.

---

## ⭐ Support

If you find this useful, please give it a star on GitHub!
