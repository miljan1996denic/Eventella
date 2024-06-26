from os import getenv
from fastapi import FastAPI
from ticketing.routers import api_router
import uvicorn
from starlette.middleware.cors import CORSMiddleware

origins = ["*"]

title = "Ticketing API"
description = "API for ticketing management"

app = FastAPI(
    title=title,
    description=description
)

def configure():
    app.include_router(api_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )

configure()

if __name__ == "__main__":
    uvicorn.run(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}
