import logging
import os
import subprocess

log = logging.getLogger(__name__)


COMMON_CLI_PARAMS: list = ['--raw']


def bw_exec(cmd, ret_encoding='UTF-8', env_vars=None):
    """
    Command line runner fgor bitwarden CLI
    """
    cmd.extend(COMMON_CLI_PARAMS)

    cli_env_vars = os.environ

    if env_vars is not None:
        cli_env_vars.update(env_vars)
    log.info(f"Executing CLI :: {' '.join(cmd)}")
    command_out = subprocess.run(cmd, capture_output=True, encoding=ret_encoding, env=cli_env_vars, check=True)

    if len(command_out.stdout) > 0:
        return command_out.stdout
    # elif len(command_out.stderr) > 0:
    return command_out.stderr


def get_current_status():
    return bw_exec("bw status".split(" "))
