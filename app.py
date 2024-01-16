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
