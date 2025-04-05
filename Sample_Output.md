Sample Output:

vbnet
Copy
Edit
Config 1 Similarity to Default: 0.8225
Config 2 Similarity to Default: 0.9123
Config 3 Similarity to Default: 0.7908
Best Tuning Config: Config 3
Interpretation:

Lower similarity = more drift from problematic Azure defaults = better noise resilience.

Config 3 (most tuned toward no background misfires) wins.

Summary Table
Feature	Setting
ASR	Deepgram (via websocket or MRCP bridge)
initialSilenceTimeoutMs	8000
endSilenceTimeoutMs	1200
sensitivity	0.4
bargeIn	Disabled
confidenceThreshold	0.65
noInputTimeout	8000
noMatchTimeout	4000
maxSpeechTimeout	10000
