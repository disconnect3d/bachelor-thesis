import os
import errno
import shlex
import subprocess


def mkdir(name):
    try:
        os.mkdir(name)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise exc


def safe_call(command, shell=False, verbose=True, pipe_err_to_out=False):
    """Fails on failed subprocess"""
    escaped_cmd = shlex.split(command)

    if verbose:
        print("###### Calling command: {}".format(command))

    kwargs = {'stderr': subprocess.STDOUT} if pipe_err_to_out else {}

    out = subprocess.check_output(escaped_cmd, shell=shell, **kwargs)

    if verbose:
        print(str(out))    

    return out

