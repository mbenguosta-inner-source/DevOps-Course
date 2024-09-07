from fastapi import FastAPI
from app.server.routes.employee import router as EmployeeRouter


app = FastAPI()
app.include_router(EmployeeRouter, tags=["Employee"], prefix="/employee")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
