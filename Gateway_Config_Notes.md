**Notes:**

| initialSilenceTimeoutMs: | 
|:-------------------------|
|Lets the prompt finish before assuming background noise is "speech." |

| endSilenceTimeoutMs: | 
|:---------------------|
| Wait for actual pause (not just split-second ambient noise). |

| sensitivity: |
|:-------------|
| Lowered to 0.4 so Deepgram ignores "low energy" background sounds. |

| bargeInEnable: |
|:---------------|
| false ensures full prompt plays before listening even starts. |

| model: |
|:-------|
| "phonecall" — this model is trained to expect noisy, low-fidelity environments. |

| punctuation: |
|:-------------|
| true — optional but makes transcripts easier to read. |
