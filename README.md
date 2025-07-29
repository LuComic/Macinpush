# Macinpush

Macinpush is a fun reminder for yourself after you've made a push with Git. Looking into how to do it, I came across a similar project git-dude, which is basically a more advanced version of this. The purpose of this project though, is just a fun reminder to take some time for yourself, get some icecream etc, after you've been coding and have contributed to something.

## Usage

Clone the repo and run the macinpush python file.

## How does it work?

It creates a Python hook file named pre-push inside the global .git-templates/hooks directory, after which the pre-push hook is executed by Git before every push and triggers a desktop notification. This will apply to all new repos that you initialize with "init". For existing repos, use this bash:

```bash
find ~ -type d -name ".git" 2>/dev/null | while read d; do
  cp "$HOME/.git-templates/hooks/pre-push" "$d/hooks/"
  chmod +x "$d/hooks/pre-push"
done
```
