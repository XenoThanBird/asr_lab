from setuptools import setup, find_packages

setup(
    name="asr_lab",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pydub",
        "pyyaml",
        "matplotlib",
        "pandas",
        "streamlit"
    ],
    entry_points={
        "console_scripts": [
            "asr-lab-batch=batch_asr_tester:main",
            "asr-lab-optimize=sensitivity_optimizer:main",
            "asr-lab-gui=asr_config_tester_app:main",
            "asr-lab-convert=convert_yaml_json:main"
        ]
    },
    author="Matthan Bird",
    description="Automated ASR Config Testing Lab for IVR/Voice Assistant Optimization",
    license="MIT",
    keywords="ASR Voice Testing IVR NLP Kore.ai Deepgram Speechmatics",
)
