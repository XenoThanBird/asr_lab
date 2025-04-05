# asr_lab
# Automatic Speech Recognition (ASR) Config Testing and Optimization Lab for Kore.ai IVR Systems.

**Created by:** Matthan Bird
**Version:** 1.0.0
**License:** MIT
**Year:** 2025

**Original Analysis:** Cost-Effective ASR Alternatives for UniMRCP + Kore.ai
The goal is something compatible, low-latency, reliable, and cheaper (or at least better-tunable).

**Here are the options I started with:**
1. Deepgram (supports MRCPv2 via custom integrations; excellent noise handling)
2. Google DialogFlow Speech/Google Cloud Speech-to-Text (can MRCP-proxy but needs gateway adaption)
3. Nvidia Riva (if you can host your own MRCP server - incredible background noise separation, but infra heavy)
4. Speechmatics (modern MRCP support, strong in noisy environments)

**Final Recommendations based on cost-effectiveness + easy integration:**
1. Deepgram, or
2. Speechmatics (slightly pricier but very noise-robust) because both cab adapt via websocket bridges easily into Kore.ai/Kore Voice Gateway (without massive backend refactor).

**Settings to Tune at Websocket Level (MRCP/Voice Gateway)**
| Settings | Description | Suggested Value |
|:---------|:------------|:----------------|
| Initial Speech Timeout (NoInputTimeout) | How long to wait for speech before NoInput triggers. | Increase (e.g., 5000 ms -> 8000 ms) |
| MaxSpeechTimeout | How long ASR keeps listening after first sound detected. | Lower slightly (to avoid background noise trailing matches) |
| Barge-In Sensitivity (bargeInEnable, bargeInThreshold) | Controls whether low volume/noise causes early interrupt. | Keep bargeInEnable=false (already non-bargeable), but tune bargeInThreshold upward. |
| Complete Silence Detection (VAD settings) | Defines what counts as 'end of speech' (background vs speech). | Tune endpointing parameters like min silence (e.g., 150 ms -> 300 ms) |
| Speech Timeout (recognitionTimeoutMs) | Timeout after first recognition event starts | Increase if prompt has long intro or needs more "think time". |

**Settings to Tune at Kore Voice Call Properties:**
| Property | Purpose | Suggested Setting |
|:---------|:--------|:------------------|
| noInputTimeout | Controls no input duration before triggering fallback | Increase |
| noMatchTimeout | How long to wait to detect a No Match after partial speech. | Increase Slightly |
| recognitionEngineParameters | Fine control for ASR-send engine-specific JSON. | Send "profanityFilter": false, "initialSilenceTimeoutMs": 8000, "endSilenceTimeoutMs": 1000 |
| confidenceThreshold | Minimum confidence to accept recognition. | Lower slightly if you suspect over-strict matching (e.g., 0.7 -> 0.6) |
| sensitivity | Some platforms expose a "sensitivity" param directly. | Lower sensitivity for background noise handling

