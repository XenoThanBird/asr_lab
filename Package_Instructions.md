**Full Packaged Instructions for Your ASR Lab Setup**
| Step	| Command |
|:------|:--------|
| Install required libraries |	pip install numpy pyyaml pydub matplotlib pandas streamlit |
|:---------------------------|:------------------------------------------------------------|
| Set up folders	| configs/ for YAMLs, backgrounds/ for background WAVs |
|:----------------|:-----------------------------------------------------|
| Run batch testing |	python batch_asr_tester.py |
|:------------------|:---------------------------| 
|Run optimizer	| python sensitivity_optimizer.py |
|:--------------|:--------------------------------|
| Launch dashboard	| streamlit run asr_config_tester_app.py |
|:------------------|:---------------------------------------|
|Convert configs YAML <-> JSON	| python convert_yaml_json.py |
