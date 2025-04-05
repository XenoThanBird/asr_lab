#bash installation
pip install numpy pydub matplotlib

import numpy as np
from pydub import AudioSegment
from pydub.generators import WhiteNoise, Sine
import matplotlib.pyplot as plt

# 1. Generate Background Noise
background_noise = WhiteNoise().to_audio_segment(duration=5000).apply_gain(-30)  # -30dB, pretty soft

# 2. Generate a Clean User Utterance (a simple tone simulating voice energy)
utterance = Sine(440).to_audio_segment(duration=2000).apply_gain(-10)  # Stronger signal

# 3. Overlay Utterance onto Noise (simulate "talking in noisy background")
combined = background_noise.overlay(utterance, position=1000)

# 4. Export files if you want to listen
background_noise.export("background_noise.wav", format="wav")
utterance.export("clean_utterance.wav", format="wav")
combined.export("combined_test.wav", format="wav")

# 5. Simulate "Sensitivity Detection"
# Assume background_noise energy = threshold
background_samples = np.array(background_noise.get_array_of_samples())
utterance_samples = np.array(utterance.get_array_of_samples())
combined_samples = np.array(combined.get_array_of_samples())

background_rms = np.sqrt(np.mean(background_samples**2))
utterance_rms = np.sqrt(np.mean(utterance_samples**2))
combined_rms = np.sqrt(np.mean(combined_samples**2))

print(f"Background RMS (energy): {background_rms:.2f}")
print(f"Utterance RMS (energy): {utterance_rms:.2f}")
print(f"Combined RMS (energy): {combined_rms:.2f}")

# 6. Fake a "sensitivity threshold" simulation
sensitivity_threshold = 1.5 * background_rms  # Set "trigger" threshold

if utterance_rms > sensitivity_threshold:
    print(">>> Utterance detected cleanly over noise.")
else:
    print(">>> Utterance NOT cleanly detected. Sensitivity tuning needed!")

# 7. Visualization
plt.figure(figsize=(10,4))
plt.plot(background_samples[:5000], label="Background Noise")
plt.plot(utterance_samples[:5000], label="Clean Utterance")
plt.plot(combined_samples[:5000], label="Combined Audio")
plt.legend()
plt.title("Simulated Audio Signals")
plt.show()
