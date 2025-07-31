#!/usr/bin/env python3
import os
import stat

# Expanduser gives the full file path
HOOKS_DIR = os.path.expanduser("~/.git-templates/hooks")
PRE_PUSH_PATH = os.path.join(HOOKS_DIR, "pre-push")

HOOK_SCRIPT = """#!/usr/bin/env python3
import subprocess
import random
import sys

list_of_choices = [
    'Go buy yourself an ice cream',
    'Enjoy some Netflix now',
    'Admire your push on GitHub',
    'Read your favourite book now',
    'Enjoy a little break now',
    'Touch some grass now'
]

for line in sys.stdin:
    local_ref, local_sha1, remote_ref, remote_sha1 = line.strip().split()
    message = subprocess.check_output(
        ['git', 'show', '--format=%B', '-s', remote_ref])

def generate_the_notification():
    chosen = random.choice(list_of_choices)
    notification_message = f'You pushed on Git!\\\\n{chosen}'
    apple_script = f'display notification "{notification_message}" with title "Macinpush"'
    subprocess.run(['osascript', '-e', apple_script])

def run():
    generate_the_notification()

if __name__ == "__main__":
    run()
"""

# The main function that creates the python file 'pre-push' 
def setup_hook():
    os.makedirs(HOOKS_DIR, exist_ok=True)
    with open(PRE_PUSH_PATH, "w") as f:
        f.write(HOOK_SCRIPT)
    # Adds to the file permissions to make it executable
    os.chmod(PRE_PUSH_PATH, os.stat(PRE_PUSH_PATH).st_mode | stat.S_IEXEC)

    # Configure Git to use this for new reops
    os.system(f'git config --global init.templatedir "{os.path.expanduser("~/.git-templates")}"')
    print(f"[+] Git global pre-push hook installed at {PRE_PUSH_PATH}")

if __name__ == "__main__":
    setup_hook()
