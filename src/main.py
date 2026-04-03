from fastapi import FastAPI

app = FastAPI(
    title="Atlas API",
    version="1.0.0"
)


@app.get("/")
def health():
    return {"status": "ok"}
