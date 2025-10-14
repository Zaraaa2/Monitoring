from fastapi import FastAPI
from routers import monitoring, router_control, nas

app = FastAPI(
    title="Router & NAS Monitoring API",
    description="Backend API untuk monitoring router, NAS, dan user management",
    version="1.0"
)

app.include_router(monitoring.router)
app.include_router(router_control.router)
app.include_router(nas.router)

@app.get("/")
def root():
    return {"message": "Backend API running successfully!"}
