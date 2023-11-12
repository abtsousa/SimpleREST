from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def print_test():
    return {"message": "Hello, world!"}
