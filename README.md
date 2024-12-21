# Godot Telegram

**Godot Telegram** is a stupid simple to use base for Godot 3/4 telegram games with everything you need.

## Core features

- **Game backend** - 🚧 Work in progress
  - 🚧 **Game config from Google Sheets** - change a table in google => change game and server behaviour 

TODO: 
- **Telegram bot**
- **Godot 3 template**
- **Godot 4 template**

## Roadmap

> 💡 This roadmap is subject to change based on project needs and community feedback. Also roadmap is not ordered.

### Backend features roadmap
- 📊 **Game config from Google Sheets** for game and server
  - ✅ Basic config that updates in real time (every request goes to google sheet)
  - Use caching and persistance for game configs
- 🤖 **Telegram bot** that signs up a **User** on backend
- 👩 **User** 🚧 Work in progress
  - profile and settings
  - score and leaderboard

### Godot roadmap
- Basic game template for Godot 3
  - Supports telegram and backend interactions
- Basic game template for Godot 4

### Tech roadmap
- Test coverage
- Linting, formating, static analysis
- CI with github-actions
- metrics/logs/sentry
- AWS deployment
- Yandex.Cloud deployment

## Setup Windows

Backend relies on WSL 2 (Ubuntu) and Docker

1) [Setup WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
2) [Install docker](https://docs.docker.com/desktop/setup/install/windows-install/)
3) Get this repo with git: `git clone https://github.com/godot-telegram/godot-telegram.git`

## Run server

1) get google api token
2) Run `make init`
3) in file `backend/.env.secret` set google api token
4) Run `make run`

For configs demo, I use public google sheets doc. For your project you should use your own.
- in file `backend/.env.secret` set google sheets doc id, get it from url of your public by link doc.

Urls:
- http://localhost:8000 - server
  - http://localhost:8000/docs/ - swagger-ui, you can try all possible requests here
  - http://localhost:8000/game_configs/ - game_configs from google sheets
- http://localhost:5432 - postgres (user: backend, password: backend, db: backend)