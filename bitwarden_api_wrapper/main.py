import os
import subprocess

import uvicorn
import yaml
import logging.config as log_config
import logging
from fastapi import FastAPI
from .secrets.bw import router

DEFAULT_CONFIG = """
logging:
  formatters:
    brief:
      format: '%(message)s'
    default:
      format: '%(asctime)s :: %(name)s:%(levelname)s :: %(module)s:%(funcName)s:%(lineno)d :: %(message)s'
  handlers:
    console:
      class: logging.StreamHandler
      formatter: default
      stream: ext://sys.stdout
    file:
      backupCount: 3
      class: logging.handlers.RotatingFileHandler
      filename: app.log
      formatter: default
      maxBytes: 1024
  loggers:
    ? ''
    : handlers:
      - console
      - file
      level: INFO
    test:
      handlers:
      - console
      level: DEBUG
  version: 1
"""

default_config = yaml.safe_load(DEFAULT_CONFIG)

if "logging" in default_config:
    log_config.dictConfig(default_config["logging"])

log = logging.getLogger(__name__)
log.info("Creating fast api app")
app = FastAPI()
log.info("Created fast api app")
log = logging.getLogger(__name__)
log.info("Starting application")

COMMON_CLI_PARAMS: list = ['--raw']


def bw_exec(cmd, ret_encoding='UTF-8', env_vars=None):
    cmd.extend(COMMON_CLI_PARAMS)

    cli_env_vars = os.environ

    if env_vars is not None:
        cli_env_vars.update(env_vars)
    print('Executing CLI :: %s' % ' '.join(cmd))
    command_out = subprocess.run(cmd, capture_output=True, encoding=ret_encoding, env=cli_env_vars)

    if len(command_out.stdout) > 0:
        return command_out.stdout
    elif len(command_out.stderr) > 0:
        return command_out.stderr


@app.get("/hello_world", tags=["hello_world_tag"], description="hello_world_description")
async def hello_world():
    return {"message": "Hello World"}


app.include_router(router)

# bitwarden_api_wrapper
# uvicorn.run("bitwarden_api_wrapper:app", host='0.0.0.0', port=4557, debug=True)
uvicorn.run(app, host='0.0.0.0', port=4557, debug=True)
