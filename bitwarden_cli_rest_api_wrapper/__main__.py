import logging
from fastapi import FastAPI
import uvicorn
from bitwarden_cli_rest_api_wrapper import bw_router


log = logging.getLogger(__name__)
app = FastAPI()
print('From bitwarden_cli_rest_api_wrapper __main__')
log.info("Starting application")


@app.get("/hello_world", tags=["hello_world_tag"], description="hello_world_description")
async def hello_world():
    return {"message": "Hello World"}


app.include_router(bw_router.router)

# bitwarden_api_wrapper
# uvicorn.run("bitwarden_api_wrapper:app", host='0.0.0.0', port=8200, debug=True)
uvicorn.run(app, host='0.0.0.0', port=8200, debug=True)
