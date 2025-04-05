import os
import yaml
import numpy as np
import pandas as pd
from pydub import AudioSegment

# Directories
config_dir = "configs/"
background_dir = "backgrounds/"
output_csv = "batch_test_results.csv"

# List YAML configs
configs = [os.path.join(config_dir, f) for f in os.listdir(config_dir) if f.endswith(".yaml")]

# List Background Audios
backgrounds = [os.path.join(background_dir, f) for f in os.listdir(background_dir) if f.endswith(".wav")]

# Results List
results = []

for config_file in configs:
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    sensitivity = config.get("recognitionEngineParameters", {}).get("sensitivity", 0.5)
    
    for bg_file in backgrounds:
        bg = AudioSegment.from_wav(bg_file)
        bg_samples = np.array(bg.get_array_of_samples())
        bg_rms = np.sqrt(np.mean(bg_samples**2))

        # Calculate threshold
        threshold = bg_rms * (1 + (1 - sensitivity))

        # Fake utterance (stronger sound)
        fake_utterance_rms = bg_rms * 2  # Assume user speech has double energy

        # Decision
        passed = fake_utterance_rms > threshold

        results.append({
            "Config": os.path.basename(config_file),
            "Background": os.path.basename(bg_file),
            "Sensitivity": sensitivity,
            "Background_RMS": round(bg_rms, 2),
            "Threshold": round(threshold, 2),
            "Utterance_RMS": round(fake_utterance_rms, 2),
            "Passed": passed
        })

# Save results
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)
print(f"Batch testing complete! Results saved to {output_csv}")
