# StudyEnglishBot
Developed on aiogram framework with wide use of aiogram-dialog library. As DB it uses PostgreSQL (SQLAlchemy)

This Telegram bot is made for people who are currently learning English language and want to 
improve their skills. Learning process includes different types of exercises.

## Getting Started
You can clone this repository by using a terminal command:
```
git clone git@github.com:David-Roklem/StudyEnglishBot.git
```

## Dependencies
All the dependencies for this project are listed in pyproject.toml and requirements.txt files.

## Installing
During the project's development [uv](https://docs.astral.sh/uv/) package manager was used.
It is preffered to create virtual environment beforehand. With uv it can be done by the command:
```
uv venv
```
For installing all the required dependencies, run:
```
uv add -r requirements.txt
```

## PostgreSQL
The code base is adapted for utilizing **PostgreSQL**. If you wish to use another database, you will need to rewrite code in order to satisfy new requirements.

## Executing program
As this project uses python-dotenv library under the hood, first of all you need to configure your `.env` with the variables
provided in `.env.example` altering them according to your needs.

To run the project on your local machine you should follow these steps:

1. configure you database, then run it (there's `docker-compose.yml` in case you want to run PostgreSQL in a container, with **adminer** as well - it may need some specific edits)
2. apply migrations to your database by the command:
```
alembic revision --autogenerate "<Migration name>"
alembic upgrade head
```
3. run bot/main.py file to start interacting with the bot