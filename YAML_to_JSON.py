pip install pyyaml

import yaml
import json

def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r') as f:
        yaml_content = yaml.safe_load(f)
    with open(json_file, 'w') as f:
        json.dump(yaml_content, f, indent=2)
    print(f"Converted {yaml_file} -> {json_file}")

def json_to_yaml(json_file, yaml_file):
    with open(json_file, 'r') as f:
        json_content = json.load(f)
    with open(yaml_file, 'w') as f:
        yaml.dump(json_content, f, default_flow_style=False)
    print(f"Converted {json_file} -> {yaml_file}")

# Example usage:
# yaml_to_json('asr_tuning_profile.yaml', 'asr_tuning_profile.json')
# json_to_yaml('asr_tuning_profile.json', 'asr_tuning_profile.yaml')
