from fastapi import FastAPI

app = FastAPI(title="VeriHome System")

@app.get("/")
async def root():
    return {"status": "VeriHome System Online"}