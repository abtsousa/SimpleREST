# Random App API

<!--toc:start-->
- [Setup](#setup)
<!--toc:end-->

## Setup

1) Setup your Python environment (e. g. with Pyenv on Linux):

```bash
pyenv local 3.12
pyenv exec python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Run the live server with uvicorn:

```bash
uvicorn RandomAppAPI.main:app --reload
```

3) Test the API by sending a GET request to the IP address of the live server (e.g. cURL):

```bash
curl http://127.0.0.1:8000/
```
