from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Define different configuration sets (initial arrays)
default_azure_config = np.array([3000, 2000, 15000, 0.75, 0.8])  # Azure Speech defaults (problematic)
ideal_config = np.array([8000, 4000, 10000, 0.65, 0.4])          # Deepgram / Speechmatics tuned
alt_config1 = np.array([6000, 3000, 12000, 0.7, 0.5])            # Moderate tuning
alt_config2 = np.array([9000, 5000, 9000, 0.6, 0.3])             # Aggressive tuning

# Stack configs for comparison
configs = np.vstack([ideal_config, alt_config1, alt_config2])

# Calculate cosine similarities
similarities = cosine_similarity([default_azure_config], configs)

# Print results
for i, score in enumerate(similarities[0]):
    print(f"Config {i+1} Similarity to Default: {score:.4f}")

# Find the best config (lowest similarity means furthest from problematic baseline)
best_index = np.argmin(similarities)
print(f"Best Tuning Config: Config {best_index+1}")
