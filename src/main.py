from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions.get_test import get_test

app = FastAPI()

##############################################################################
# add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")
# static_files_app = StaticFiles(directory=".")
# app.mount(path="/static", app=static_files_app, name="static")
##############################################################################

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Definimos rutas

@app.get("/test")
async def root():
    return (get_test())