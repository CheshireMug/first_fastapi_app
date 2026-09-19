from fastapi import FastAPI

app = FastAPI(title="My First Project")


@app.get("/example")
async def example():
    return {"message": "Hello"}
