from fastapi import FastAPI
from path_parameters import include_path_router
from query_parameters import include_query_router

app = FastAPI()

include_path_router(app)
include_query_router(app)