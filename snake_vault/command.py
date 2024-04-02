#! /usr/bin/env python
## ----------------------------------------------------------------------- INFO
## [command.py]
## author        : fantomH @alterEGO Linux
## created       : 2023-12-08 11:52:32 UTC
## updated       : 2023-12-20 14:30:28 UTC
## description   : Commands utils

from collections import namedtuple
import shlex
import shutil
import subprocess

def execute(cmd, cwd=None, shell=False, capture_output=False, stdout=subprocess.PIPE, text=True, input=None):
    # :version       : 2024-03-30 02:50:48 UTC
    # :description   : A custom function to run subprocess

    """Simplyfied subprocess.run.

    Arguments:
        cmd: (str) Command to be executed.
             If the command includes variables or input, use f-string.
             Example:
                hello = "Hello world"
                execute(f"echo {hello}")
             If the command includes pipes, or other shell characters, set the 
             argument `shell` to True. See shell.
        cwd: (str) Current working directory.
             If you need to run the command in a particular directory.
        shell: (bool) Run command as in the terminal. Default: False
             By default the `cmd` is split as a list, using shlex.
             Set `shell` to True if you have any shell reserved characters,
             such as pipes or redirections.
             Example:
                execute(f"find / -iname *password* 2>/dev/null | grep '/usr/share'", shell=True)
        capture_output: (bool) Capture the command stdout and stderr. Default: False.
                        Use this only to parse the stdout and stderr.
                        Terminal interaction will be impossible.
        text:
        input: (str) Takes a string the command need to injest.
    """

    if shell == True:
        cmd_list = cmd
    else:
        cmd_list = shlex.split(cmd)
    if input:
        input = input.encode()

    if capture_output:
        stdout=None
        
    cmd_run = subprocess.run(cmd_list, cwd=cwd, shell=shell, capture_output=capture_output, stdout=stdout, input=input)

    CommandResults = namedtuple('CommandResults', ['returncode',
                                                   'stdout',
                                                   'stderr',
                                                   'args',
                                                   'cwd',
                                                   'input'])

    result = CommandResults(cmd_run.returncode, cmd_run.stdout, cmd_run.stderr, cmd_run.args, cwd, input)
    return result

def which(exec_list: list) -> bool:

    for e in exec_list:
        if shutil.which(e) is None:
            return False

    return True

if __name__ == "__main__":

    print(execute('sudo pacman -Syu', capture_output=False))

    subprocess.run('sudo pacman -Syu', shell=True, capture_output=True)
    # print(which(["bat", "bash", "hello"]))

    # print(execute.__doc__)
    # xec = execute(f"paru -S --noconfirm nightpdf-git")

    # print(xec.stdout)

# _input = "hello world"
# results = execute(f"paru -Qlq paru", capture_output=True, cwd="/tmp", input=_input)

# print(results.cwd, results.input, results.args)


# vim: foldmethod=marker
## ------------------------------------------------------------- FIN ¯\_(ツ)_/¯
