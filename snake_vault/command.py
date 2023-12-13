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
    """Simplyfied subprocess.run.

    Arguments:
        cmd: (str) Command to be executed.
             If the command includes variables or input, use f-string.
             Example:
                hello = "Hello world"
                execute(f"echo {hello}")
             If the command includes pipes, or other shell characters, set the 
             argument `shell` to True.
             Example:
                execute(f"find / -iname *password* 2>/dev/null | grep '/usr/share'", shell=True)
        cwd: (str) Current working directory.
             If you need to run the command in a particular directory.
        shell: (bool) Run command as in the terminal. Default: False
             By default the `cmd` is split as a list, using shlex.
             Set `shell` to True if you have any shell reserved characters,
             such as pipes or redirections.
        capture_output: (bool) Capture the command stdout and stderr. Default: False.
        text:
        input: (str) Takes a string the command need to injest.
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

if __name__ == "__main__":

    print(execute.__doc__)
    xec = execute(f"paru -S --noconfirm nightpdf-git")

    print(xec.stdout)

# _input = "hello world"
# results = execute(f"paru -Qlq paru", capture_output=True, cwd="/tmp", input=_input)

# print(results.cwd, results.input, results.args)


# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
