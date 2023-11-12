# Random App API

<!--toc:start-->

- [Setup](#setup)
- [Run](#Run)
- [Test](#Test)
<!--toc:end-->

## Setup

1. Clone this repository to the directory of your choice (e.g. Github CLI):

```bash
gh repo clone abtsousa/SimpleREST
```

2. On that directory setup your Python environment (e. g. with Pyenv on Linux):

```bash
pyenv local 3.12
pyenv exec python -m venv .venv
source .venv/bin/activate
```

3. Install related dependencies:

```bash
pip install -r requirements.txt
```

## Run

Run the live server with uvicorn:

```bash
uvicorn RandomAppAPI.main:app --reload
```

## Test

In a separate terminal window test the API by sending a GET request to the IP address of the live server (e.g. cURL):

```bash
curl -i http://127.0.0.1:8000/suggest_app
```

You should get a `HTTP/1.1 200 OK` header followed by a JSON response, such as this:

```text
HTTP/1.1 200 OK
date: (...)
server: uvicorn
content-length: 41
content-type: application/json

{"app_name":"Lords Mobile: Kingdom Wars"}%
```

## Full documentation

While running the server the documentation can be checked at /docs:

http://127.0.0.1:8000/docs
