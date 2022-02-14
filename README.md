# Entity Recognition Bot

A bot that recognises entity from user utterance and displays its definition.

## Prerequisites

- Python 3.6 or higher

## Running the project

- Run `python -m venv venv` to create a virtual environment
- For Windows, run `venv\Scripts\activate` to activate virtual environment.
- For Linux, run `source venv/bin/activate` to activate virtual environment.
- Run `pip install -r requirements.txt` to install all dependencies.
- Create a `.env` file from `example.env` file and fill necessary values.
- Run `python app.py`

## Testing the bot using Bot Framework Emulator

- Install the Bot Framework Emulator version 4.3.0 or greater
  from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://{HOST}:{PORT}/api/messages`

