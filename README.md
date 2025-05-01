# Math LLM Playground

This project is to play around with different LLMs for math solution evaluation. 

## Hardware and software 

Documenting what system I used to run the project. 

- OS: Linux Mint
- NVIDIA-SMI 535.183.01
- Driver Version: 535.183.01
- CUDA Version: 12.2     
                                                                                         

## Run project

Create a virtual env

```
python3 -m venv .env
```

Activate the virtual env
```
source .env/bin/activate
```

Install requirement packages
```
pip install -r requirements.txt
```

Run scripts
```
python3 path-to-the-script
```

## Evaluation of models

The evalutions are done by feeding maths question and answer pairs to the model and compare the outputs. 

Under the prompts folder, there are 6 modules.

prompts
L algebra.py
L geometry.py
L measurement.py
L number.py
L probability.py
L statistics.py

This is matching the maths topics defined by [New Zealand government website](https://newzealandcurriculum.tahurangi.education.govt.nz/5637238339.p).