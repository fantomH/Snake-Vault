#! /usr/bin/env python
## ----------------------------------------------------------------------- INFO
## [command.py]
## author        : fantomH @alterEGO Linux
## created       : 2023-12-08 11:52:32 UTC
## updated       : 2023-12-12 13:03:39 UTC
## description   : Commands utils

from collections import namedtuple
import shlex
import subprocess

def execute(cmd, cwd=None, shell=False, capture_output=False, text=True, input=None):
    """
    Simplyfied subprocess.run.

    ARGS:
        cmd: (str) Command to be executed.
             If the command includes variables or input, use f-string.
             Example:
                hello = "Hello world"
                execute(f"echo {hello}")
             If the command includes pipes, or other shell characters, set the 
             argument `shell` to True.
    """

    if shell == True:
        cmd_list = cmd
    else:
        cmd_list = shlex.split(cmd)
    if input:
        input = input.encode()
        
    cmd_run = subprocess.run(cmd_list, cwd=cwd, shell=shell, capture_output=capture_output, input=input)

    CommandResults = namedtuple('CommandResults', ['returncode',
                                                   'stdout',
                                                   'stderr',
                                                   'args',
                                                   'cwd',
                                                   'input'])

    cmd = CommandResults(cmd_run.returncode, cmd_run.stdout, cmd_run.stderr, cmd_run.args, cwd, input)
    return cmd

# _input = "hello world"
# results = execute(f"paru -Qlq paru", capture_output=True, cwd="/tmp", input=_input)

# print(results.cwd, results.input, results.args)

print(execute.__doc__)

# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
