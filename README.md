## Dashboard-auto-reload

A python script providing an idea of how a MindSphere application, e.g., a dashboard, can be displayed around the clock without the need of manual re-authentication on enforced session expiration.

#### How it works
The script starts a new incognito Chrome window, logs into MindSphere and navigates to the configured dashboard's URL. As soon as the pre-configured ```reloadAfterSec``` seconds elapse, the Chrome window is closed and everything starts from the beginning. 
Along with the ```reloadAfterSec```, the configuration file contains the URL to navigate to, MindSphere username and password:
```
{
  "url": "<dashboard's URL>",
  "user": {
    "email": "<MindSphere User>",
    "password": "<Password>"
  },
  "reloadAfterSec": 10800
}
```

Please note that the script works with the default MindSphere IDP and have to be adjusted if you set up a custom IDP.

### Prerequisites:

- [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/latest/installation/)
- [python selenium](https://selenium-python.readthedocs.io/installation.html)
- [chrome driver](https://chromedriver.chromium.org/downloads) matching the Chrome browser

Put the chrome driver next to the script, so that it looks like:
```
|--dashboard-auto_reload
    |--   auto_reload.py
    |--   chromedriver.exe
    |--   config.json
```
### How to use
To start the script just start the python while passing the script as a command line argument:
```
python auto_reload.py
```

