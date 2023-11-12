# Random App API

<!--toc:start-->
- [Setup](#setup)
<!--toc:end-->

## Setup

1) Clone this repository to the directory of your choice.

2) On that directory setup your Python environment (e. g. with Pyenv on Linux) and install related dependencies:

```bash
pyenv local 3.12
pyenv exec python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Run the live server with uvicorn:

```bash
uvicorn RandomAppAPI.main:app --reload
```

## Test

3) Test the API by sending a GET request to the IP address of the live server (e.g. cURL):

```bash
curl -i http://127.0.0.1:8000/suggest_app
```

## Full documentation

After running the server the documentation can be checked at /docs:

http://127.0.0.1:8000/docs


