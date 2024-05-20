# :----------------------------------------------------------------------- INFO
# :[Snake-Vault/snake_vault/command.py]
# /author        : fantomH
# /created       : 2023-12-08 11:52:32 UTC
# /updated       : 2024-05-20 21:27:36 UTC
# /description   : Commands utils

from collections import namedtuple
import shlex
import shutil
import subprocess

def execute(cmd, cwd=None, shell=False, text=True, input=None, interact=False):

    """(function) execute()

    A custom function to run subprocess

    Arguments:
        cmd: (str) Command to be executed.
             If the command includes variables or input, use f-string.
             Example:
                hello = "Hello world"
                execute(f"echo {hello}")
             By default, the string will be split into a list, using shlex.split
             to satisfy subprocess function.
             If the command includes pipes, or other shell characters, set the 
             argument `shell` to True. See shell.
        cwd: (str, default: None) Current working directory.
             If you need to run the command in a particular directory.
        shell: (bool, default: False) Run command as in the terminal.
             Set `shell` to True if you have any shell reserved characters,
             such as pipes or redirections.
             Example:
                execute(f"find / -iname *password* 2>/dev/null | grep '/usr/share'", shell=True)
        text: (bool, default: True) stdout, stderr as string, not bytes.
        input: (str, default: None) Takes a string the command need to injest.
             Input will be encoded to satisfy subprocess.
        interact: (bool, default: False) In order to interact with a subprocess,
             capture_output must be disabled. Thus, you cannot capture the 
             stdout and stderr, and run the subprocess with manual intervention
             at the same time.
    """

    # :Shell
    if shell == True:
        cmd_list = cmd
    else:
        cmd_list = shlex.split(cmd)

    # :Standard input.
    if input:
        input = input.encode()

    # :Interact
    if interact:
        capture_output = False
    else:
        capture_output = True
        
    cmd_run = subprocess.run(cmd_list, cwd=cwd, shell=shell, input=input, capture_output=capture_output)

    CommandResults = namedtuple('CommandResults', ['returncode',
                                                   'stdout',
                                                   'stderr',
                                                   'args',
                                                   'cwd',
                                                   'input'])

    result = CommandResults(cmd_run.returncode, cmd_run.stdout, cmd_run.stderr, cmd_run.args, cwd, input)
    return result

def which(exec_list: list) -> bool:

    """(function) which()

    Verify a list of executable if exist on the system.

    Arguments:
        exect_list: (list) Executable list.
    """

    if not isinstance(exec_list, list):
        return 'You must provide a list of executable.'

    for e in exec_list:
        if shutil.which(e) is None:
            return False

    return True
