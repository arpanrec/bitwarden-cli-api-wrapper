__version__ = '0.0.1'
import yaml
import logging.config as log_config

print('From bitwarden_cli_rest_api_wrapper __init__')
print('bitwarden_cli_rest_api_wrapper version:', __version__)

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
