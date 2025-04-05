pip install streamlit

import streamlit as st
import numpy as np
import yaml
from pydub import AudioSegment
from io import BytesIO

# Title
st.title("ASR Config Tester (Mini Lab)")

# Upload YAML Config
st.header("1. Upload Your YAML Config")
yaml_file = st.file_uploader("Upload YAML File", type=["yaml"])
config = None

if yaml_file:
    config = yaml.safe_load(yaml_file)
    st.success("YAML Loaded!")
    st.json(config)

# Upload Audio Samples
st.header("2. Upload Audio Samples")
background_file = st.file_uploader("Upload Background Noise Audio", type=["wav"], key="background")
utterance_file = st.file_uploader("Upload Utterance Audio", type=["wav"], key="utterance")

# Run Test
if st.button("Run ASR Sensitivity Test"):
    if config and background_file and utterance_file:
        # Load audio files
        background = AudioSegment.from_wav(background_file)
        utterance = AudioSegment.from_wav(utterance_file)

        # Convert to samples
        background_samples = np.array(background.get_array_of_samples())
        utterance_samples = np.array(utterance.get_array_of_samples())

        # RMS energy
        background_rms = np.sqrt(np.mean(background_samples**2))
        utterance_rms = np.sqrt(np.mean(utterance_samples**2))

        st.write(f"Background RMS: {background_rms:.2f}")
        st.write(f"Utterance RMS: {utterance_rms:.2f}")

        # Read Sensitivity from YAML
        sensitivity = config.get("recognitionEngineParameters", {}).get("sensitivity", 0.5)
        threshold = background_rms * (1 + (1 - sensitivity))

        st.write(f"Sensitivity Threshold: {threshold:.2f}")

        # Decision
        if utterance_rms > threshold:
            st.success("Result: Utterance detected cleanly over background noise.")
        else:
            st.error("Result: Utterance might be drowned by background noise. Consider adjusting sensitivity.")
    else:
        st.error("Please upload all required files.")

