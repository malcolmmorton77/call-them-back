# Malcolm M.

## About this project

- to create a virtual environment with all the dependencies involved, I used the command `virtualenv [name]`
- run `source [name]/bin/activate`
- next, run `pip install twilio==5.7.0` to install the twilio pkgs
- I wanted to create this to begin robo-dialling back the scam calls

# Fixes

- `~/python3.10/site-packages/twilio/rest/resources/imports.py` was altered to grab the updated packages, since I was getting an Import not Found Error

```python
  try:
    from urllib.parse import parse_qs
  except ImportError:
    from cgitb import parse_qs
```

# Instructions to run:

You will want a virtual environment, with installed dependencies

```bash
  virtualenv [name]
  source /[name]/bin/activate
  pip install twilio==5.7.0
```

You will also need to setup Twilio with an account and add your config file to the directory

```
  vim config.py
  //add your twilio phone number, your personal number, the Account SID and Account Token
```

To execute my program:

```python3
  python3 phone_calls.py
```
