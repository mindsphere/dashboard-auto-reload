## Dashboard-Helper

A python script providing an idea of how a MindSphere application, e.g., a dashboard, can be displayed around the clock without the need of manual re-authentication on enforced session expiration.

#### How it works
The script starts a new incognito Chrome window and uses the data provided in ```config.json``` to login into MindSphere and to navigate to the configured dashboard's URL. As soon as the ```reloadAfterSec``` seonds elapse, the Chrome window is closed and everything starts from the beginning. 
Along with the ```reloadAfterSec```, the configuration file contains the URL to navigate to, MindSphere username and password:
```
{
  "url": "<dashbord's URL>",
  "user": {
    "email": "<MindSphere User>",
    "password": "<Password>"
  },
  "reloadAfterSec": 10800
}
```

### Prerequisites:

- [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/latest/installation/)
- [python selenium](https://selenium-python.readthedocs.io/installation.html)
- [chrome driver](https://chromedriver.chromium.org/downloads) matching the Chrome browser

Put the chrome driver next to the script, so that it looks like:
```
|--dashboard-helper
    |--   auto_reload.py
    |--   chromedriver.exe
    |--   config.json
```
### How to use
To start the script just start the python while passing the script as a comand line argument:
```
python auto_reload.py
```

