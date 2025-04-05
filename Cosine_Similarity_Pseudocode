**Interpretation:**
1. If similarity is low, it means the current configuration differs greatly
2. If similar is high, it means you need to move farther from defaults

**Written in Python:** 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Prompted Settings (ideal conditions)
ideal_settings = np.array([8000, 4000, 10000, 0.65, 0.5])

# Current Azure Speech Defaults (problematic)
current_settings = np.array([3000, 2000, 15000, 0.75, 0.8])

#Calculate Cosine Similarity (how similar the tuned settings are to defaults)
similarity = cosine_similarity([ideal_settings], [current_settings])

print(f"Cosine Similarity Score: {similarity[0] [0]}")
