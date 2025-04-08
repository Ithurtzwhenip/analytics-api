from typing import Union
from fastapi import FastAPI
from api.events import router as event_router
from contextlib import asynccontextmanager
from api.db.session import init_db
from fastapi.middleware.cors import CORSMiddleware

import os
print("✅ Starting app with DATABASE_URL =", os.getenv("DATABASE_URL"))

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("🔥 Running init_db()")
        init_db()
        print("✅ init_db() complete")
    except Exception as e:
        print("❌ Error in init_db():", e)
    yield



app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(event_router, prefix="/api/events")


@app.get("/")
def read_root():
    print("👋 Root endpoint hit")
    return {"Hello": "World"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}
