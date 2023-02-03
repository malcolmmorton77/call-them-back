# Malcolm M.

# About this project

- I wanted to create this to begin robo-dialling back the scammer calls

# Fixes

- `~/python3.10/site-packages/twilio/rest/resources/imports.py` was altered to grab the updated packages, since I was getting an Import not Found Error

```python
  > # parse_qs
  >
  > try:
  >   from urllib.parse import parse_qs
  > except ImportError:
  >   from cgitb import parse_qs
```
