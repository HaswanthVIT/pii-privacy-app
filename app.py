import streamlit as st
from transformers import pipeline, CLIPProcessor, CLIPModel
from PIL import Image
import torch, hashlib, secrets, base64, io, re

st.set_page_config(page_title="AQSPF Dashboard", layout="wide")

# --- Models ---
@st.cache_resource
def load_models():
    ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
    clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    clip_proc = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    return ner, clip_model, clip_proc

pii_detector, clip_model, clip_processor = load_models()

# --- Quantum Privacy Simulation ---
def quantum_privacy_score(text_conf, img_conf):
    # simplified: quantum_refined_conf = sigmoid(weighted mean)
    q_ref = (float(text_conf) + float(img_conf)) / 2
    # convert to tensor before torch math
    q_tensor = torch.tensor(q_ref, dtype=torch.float32)
    privacy = (1 / (1 + torch.exp(-8 * (q_tensor - 0.5)))).item()
    return q_ref, privacy

# --- PQC Simulation ---
def pqc_encrypt(text):
    sk = secrets.token_bytes(32)
    pk = hashlib.sha256(sk).digest()
    rnd = secrets.token_bytes(32)
    shared = hashlib.sha256(pk + rnd).digest()
    sym_key = hashlib.sha256(shared).digest()
    enc = bytes([b ^ sym_key[i % len(sym_key)] for i, b in enumerate(text.encode())])
    dec = bytes([b ^ sym_key[i % len(sym_key)] for i, b in enumerate(enc)])
    return base64.b64encode(enc).decode(), dec.decode()

# --- Streamlit UI ---
st.title("🧠 Agentic Quantum-Safe Privacy Framework (AQSPF)")
st.markdown("### Upload Text or Image to Analyze and Protect PII")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Textual PII Detection")
    user_text = st.text_area("Enter sample text",
        "Just moved into my new flat near Signal Café in Bangalore! Contact me at jonyd1234@gmail.com or call +91-9876543210.")
    
    if st.button("Detect PII"):
        result = pii_detector(user_text)
        
        # --- Regex-based PII detection (phones, emails, spelled-out numbers) ---
        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", user_text)
        phones = re.findall(r"\+?\d[\d\-\s]{8,}\d", user_text)
        words = re.findall(r"\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\b", user_text.lower())
        
        if emails:
            result.append({"entity_group": "EMAIL", "word": ", ".join(emails), "score": 0.99})
        if phones or words:
            combined = " ".join(phones) if phones else " ".join(words)
            result.append({"entity_group": "PHONE", "word": combined, "score": 0.95})
        
        # Display combined results
        st.write(result)
        
        if result:
            conf = max([float(r["score"]) for r in result])
            st.success(f"Detected entities with confidence {conf:.3f}")
            st.session_state.text_conf = conf
        else:
            st.warning("No entities detected.")
            st.session_state.text_conf = 0.0

with col2:
    st.subheader("Image PII Detection (CLIP)")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg","png"])
    labels = ["credit card","id card","passport","document","person"]
    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")
        st.image(img, caption="Uploaded image", use_container_width=True)
        inputs = clip_processor(text=labels, images=img, return_tensors="pt", padding=True)
        with torch.no_grad():
            logits = clip_model(**inputs).logits_per_image
            probs = logits.softmax(dim=1)[0]
        for label, p in zip(labels, probs):
            st.write(f"{label:12s} → {p.item():.3f}")
        conf = torch.max(probs).item()
        st.session_state.img_conf = conf
        st.success(f"Most likely content: {labels[torch.argmax(probs)]} (conf {conf:.3f})")

st.markdown("---")

if "text_conf" in st.session_state and "img_conf" in st.session_state:
    st.subheader("Quantum Privacy Evaluation")
    qc, priv = quantum_privacy_score(st.session_state.text_conf, st.session_state.img_conf)
    st.info(f"Quantum-refined confidence: {qc:.3f}")
    st.success(f"Suggested privacy level: {priv:.3f}")
    
    st.subheader("PQC Encryption (Simulated Kyber)")
    enc, dec = pqc_encrypt(f"REDACTED: {user_text}")
    st.code(enc[:80] + "...", language="text")
    st.caption("Encrypted payload (base64 excerpt)")
    st.write("Decrypted text preview:", dec)
