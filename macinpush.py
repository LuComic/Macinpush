import subprocess
import random
import shlex

list_of_choices = [
  'Go buy youself and icecream!',
  'Enjoy some Netflix now',
  'Admire your push on Github',
  'Read your favourite book now',
  'Enjoy a little break now'
]

def run():
    chosen = random.choice(list_of_choices)
    notification_message = f'You pushed on Git!\n{chosen}'
    new_message = notification_message.replace('"', '\"')
    apple_script = f'display notification "{new_message}" with title "Macinpush"'
    
    subprocess.run(['osascript', '-e', apple_script])

if __name__ == "__main__":
    run()