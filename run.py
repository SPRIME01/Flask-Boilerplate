#!./.venv/bin/python3

from Application import app
from flask_boilerplate_utils.commands import MainManager
manager = MainManager(app,with_default_commands=False)

if __name__ == "__main__":
    manager.run(default_command="server")