from fastapi import FastAPI, Request
from routers import books, users
from database import Base, engine
import models as models
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
import time
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncSession(engine) as session:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Request processing time: {process_time:.4f} seconds")
    return response

# Lets Plug the mini-app into the main app
app.include_router(books.router)
app.include_router(users.router)  # Include the users router as well

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)