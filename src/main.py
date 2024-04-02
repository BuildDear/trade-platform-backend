from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from src.database import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
