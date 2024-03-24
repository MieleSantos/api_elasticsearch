from fastapi import FastAPI
from router import searchs

app = FastAPI(
    title="Api para buscas no Elastisearch",
    version="0.0.1",
    description="Uma Api para estudos do Elastisearch",
)

app.include_router(searchs.router, tags=["search"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", reload=True, port=8000)
