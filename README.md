# 🧠 Agentic Quantum-Safe Privacy Framework (AQSPF)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pii-privacy-app.streamlit.app/)

An AI-powered privacy protection system that detects Personally Identifiable Information (PII) in text and images, then applies quantum-inspired privacy scoring and post-quantum cryptography (PQC) encryption.

## 🚀 Live Demo

**Try it now:** [https://pii-privacy-app.streamlit.app/](https://pii-privacy-app.streamlit.app/)

## ✨ Features

### 1. **Textual PII Detection**
- Detects names, locations, and organizations using BERT-based Named Entity Recognition
- Regex-based detection for emails, phone numbers, and spelled-out numbers
- Real-time confidence scoring

### 2. **Image PII Detection**
- Uses OpenAI's CLIP model for multimodal analysis
- Identifies sensitive documents: credit cards, ID cards, passports, documents
- Visual confidence scoring for each category

### 3. **Quantum Privacy Evaluation**
- Combines text and image confidence scores
- Quantum-inspired privacy level calculation
- Suggests appropriate anonymization strength

### 4. **Post-Quantum Cryptography (PQC)**
- Simulated Kyber-based encryption
- Hash-based key exchange demonstration
- XOR cipher with derived symmetric keys

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **NLP Model:** BERT (dslim/bert-base-NER)
- **Vision Model:** CLIP (openai/clip-vit-base-patch32)
- **Framework:** PyTorch, Transformers
- **Cryptography:** Hashlib, Secrets (Python standard library)

## 📋 Requirements

```txt
transformers==4.57.1
torch>=2.0.0
torchvision
pillow
streamlit>=1.51.0
accelerate
sentencepiece
protobuf
```

## 🚦 How to Use

1. **Text Analysis:**
   - Enter or paste text containing potential PII
   - Click "Detect PII"
   - View detected entities with confidence scores

2. **Image Analysis:**
   - Upload an image (JPG/PNG)
   - View similarity scores for sensitive document types
   - See the most likely content classification

3. **Privacy Assessment:**
   - Automatic quantum-refined confidence calculation
   - Suggested privacy level (0-1 scale)

4. **Encryption Preview:**
   - View simulated PQC encryption of detected PII
   - See encrypted payload (base64 encoded)
   - Decryption preview to verify integrity

## 💻 Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/aqspf-privacy-app.git
cd aqspf-privacy-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🔬 Project Background

This project was developed as part of a data privacy research initiative exploring:
- AI-powered PII detection in multimodal data
- Quantum-inspired privacy scoring mechanisms
- Post-quantum cryptography readiness

**Original Development:** Google Colab Notebook  
**Production Deployment:** Streamlit Cloud

## 📊 Model Information

### BERT NER Model
- **Model:** dslim/bert-base-NER
- **Task:** Named Entity Recognition
- **Entities:** PER (Person), LOC (Location), ORG (Organization)

### CLIP Model
- **Model:** openai/clip-vit-base-patch32
- **Task:** Zero-shot image classification
- **Use Case:** Sensitive document detection

## ⚠️ Limitations

- First load may take 1-2 minutes (downloading AI models)
- App sleeps after 7 days of inactivity on free tier
- Quantum computing simulation (not production-grade)
- Educational/research purpose - not for production security

## 🔐 Privacy Notice

- No data is stored or transmitted
- All processing happens in-memory during your session
- Models run locally on Streamlit's infrastructure
- Your uploaded images and text are not saved

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Developed with ❤️ for advancing privacy-preserving AI technologies

## 🔗 Links

- **Live App:** [https://pii-privacy-app.streamlit.app/](https://pii-privacy-app.streamlit.app/)
- **GitHub Repository:** [[Repo URL]](https://github.com/HaswanthVIT/pii-privacy-app)
- **Documentation:** [Streamlit Docs](https://docs.streamlit.io)

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**⭐ If you find this project useful, please give it a star on GitHub!**
