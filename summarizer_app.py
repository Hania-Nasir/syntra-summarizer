# summarizer_app.py

import streamlit as st
from transformers import pipeline
import torch

# Page Configuration
st.set_page_config(
    page_title="Syntra.ai Summarizer",
    page_icon="🧠"  )

st.title("🧠 Syntra.ai – AI Text Summarizer")
st.markdown("Summarize long articles into short, clear insights using AI.")

# Load Summarization Pipeline with a lightweight model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_summarizer()

# User Input
text = st.text_area("📜 Paste your article or text here", height=300, max_chars=2000)

# Button Click
if st.button("🔍 Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Generating summary..."):
            try:
                summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
                st.subheader("📝 Summary")
                st.success(summary[0]['summary_text'])
            except RuntimeError as e:
                st.error("❌ Error: Not enough memory. Try reducing input length or reload the app.")
                st.exception(e)

st.markdown("---")
st.caption("Built by Hanya Nasir • Syntra.ai © 2025")

