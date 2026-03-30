from fastapi import FastAPI
from app.routers.compliance import router as compliance_router

app = FastAPI(title="VeriHome System")

# Include the new compliance router
app.include_router(compliance_router)

@app.get("/")
async def root():
    return {"status": "VeriHome System Online"}