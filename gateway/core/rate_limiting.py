import os
import time
import redis
from fastapi import HTTPException, status
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimiter:
    def __init__(self, redis_host: str, redis_port: int):
        self.redis_pool = redis.ConnectionPool(host=redis_host, port=redis_port, db=0, decode_responses=True)

    def get_redis(self):
        return redis.Redis(connection_pool=self.redis_pool)

    def is_rate_limited(self, key: str, max_requests: int, window: int) -> bool:
            current = int(time.time())
            window_start = current - window
            redis_conn = self.get_redis()
            with redis_conn.pipeline() as pipe:
                try:
                    pipe.zremrangebyscore(key, 0, window_start)
                    pipe.zcard(key)
                    pipe.zadd(key, {current: current})
                    pipe.expire(key, window)
                    results = pipe.execute()
                except redis.RedisError as e:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail=f"Redis error: {str(e)}"
                    ) from e
            return results[1] >= max_requests
    
class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.rate_limiter = RateLimiter("redis", 6379)

    async def dispatch(self, request: Request, call_next):
        max_requests = os.getenv("RATE_LIMITING_MAX_REQUESTS")
        window = os.getenv("RATE_LIMITING_WINDOW")

        key = f"rate_limit:{request.client.host}:{request.url.path}"
        if self.rate_limiter.is_rate_limited(key, int(max_requests), int(window)):
            return JSONResponse({"message": "Too many requests"}, status_code=429)

        # Continue handling the request
        response = await call_next(request)

        return response