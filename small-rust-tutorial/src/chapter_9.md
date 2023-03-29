# Chapter 9:  AI Pair Assisted Programming and Big Data Storage

## Mini-Lecture A:  Using GitHub Copilot CLI

* [github-copilot-cli](https://www.npmjs.com/package/@githubnext/github-copilot-cli)

tldr: these are the commands

```bash
#!/usr/bin/env bash

#some setup stuff for the dev environment
#install nodejs
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\
sudo apt-get install -y nodejs

#install GitHub Copilot CLI
npm install -g @githubnext/github-copilot-cli

#authenticate with GitHub Copilot
github-copilot-cli auth

#Upgrade
#npm install -g @githubnext/github-copilot-cli
```

* [Watch Copilot Video Link](https://youtube.com/live/F67rjOjEQE4)  
<iframe width="560" height="315" src="https://www.youtube.com/embed/F67rjOjEQE4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Suggestion:  Try out commands via `??` and put them into a `cmd.sh` so you can save both prompt and command
Here is an example of a `cmd.sh`

```bash
### GitHub Copilot Commands
## Prompt: ?? find all large rust target folders and get size and location
## CMD:  find . -name "target" -type d -exec du -sh {} \;

## Prompt:  ?? delete all rust build directories to save space
## CMD: find . -name "target" -type d -exec rm -rf {} \;
```
