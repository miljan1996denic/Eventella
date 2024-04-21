import uvicorn
from fastapi import FastAPI
from gateway.core.rate_limiting import RateLimiterMiddleware
from gateway.routers import api_router
from starlette.middleware.cors import CORSMiddleware

origins = ["*"]

title = "API Gateway"
description = "API Gateway with example of authentication and routing"

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
    app.add_middleware(RateLimiterMiddleware)

configure()

if __name__ == "__main__":
    uvicorn.run(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}
