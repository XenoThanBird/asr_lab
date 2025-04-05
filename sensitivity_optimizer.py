import numpy as np
from pydub import AudioSegment

# Load your sample files
background = AudioSegment.from_wav("background_noise.wav")
utterance = AudioSegment.from_wav("clean_utterance.wav")

# Samples
background_samples = np.array(background.get_array_of_samples())
utterance_samples = np.array(utterance.get_array_of_samples())

# RMS values
background_rms = np.sqrt(np.mean(background_samples**2))
utterance_rms = np.sqrt(np.mean(utterance_samples**2))

# Try different sensitivities
best_sensitivity = None

for sensitivity in np.linspace(0.1, 0.9, 80):  # Test from 0.1 to 0.9
    threshold = background_rms * (1 + (1 - sensitivity))
    if utterance_rms > threshold:
        best_sensitivity = sensitivity
        break  # First one that works

if best_sensitivity:
    print(f"Optimal Sensitivity Found: {round(best_sensitivity, 2)}")
else:
    print("No suitable sensitivity found. Utterance too weak compared to background.")
