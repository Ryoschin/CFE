# Getting started

In order to set everything up, do the following:

- Set `python app.py` as the startup command
- Create an app.py file, with the following contents:

```python
import subprocess

dependencies = [
    "requests",
    "cloudscraper",
    "httpx",
    "beautifulsoup4",
    "pyyaml",
    "rich",
    "pyjwt",
    "imaplib2",
]

subprocess.check_call(["git", "clone", "https://github.com/Ryoschin/CFE.git"])
subprocess.check_call(["pip", "install"] + dependencies)
```

- Run the server for the first time, it will clone the repository and install the dependencies

And, to use the program:

- Open CFE/config/config.yaml and enter your information
- Set the following command as the startup command: `python CFE/src/main.py`
- Run the server for the second time, and you're ready to go!
