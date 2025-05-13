## Dashboard auto-reload

This Python script can be used to display an Insights Hub application, such as a Dashboard Designer dashboard, 24/7 without the need for manual re-authentication when the session expires.

#### How it works
The script launches a new incognito Chrome window, logs into Insights Hub and navigates to the configured dashboard's URL. Once the pre-configured ```reloadAfterSec``` seconds have elapsed, the Chrome window closes and everything starts again. In addition to the ```reloadAfterSec```, the configuration file contains the URL to navigate to (e.g. the dashboard URL), and the Insights Hub username and password:
```
{
  "url": "<dashboard URL>",
  "user": {
    "email": "<user>",
    "password": "<password>"
  },
  "reloadAfterSec": 10800
}
```

Please note: 
1) The script works with the default Insights Hub IDP and will need to be adjusted if you set up a custom IDP
2) The Insights Hub user will need to be whitelisted, to suppress 2-factor authentication enforcement (which will not work for this automated use case)
   Please contact Insights Hub customer support to request whitelisting. Include this Github URL as a reference in your request.
3) Ensure that the PC/device used to run this script is protected from physical or remote access to reduce the risk of credential misuse.

### Prerequisites:

- [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/latest/installation/)
- [python selenium](https://selenium-python.readthedocs.io/installation.html)
- [chrome driver](https://chromedriver.chromium.org/downloads) matching the Chrome browser

Put the chrome driver next to the script in the same folder, so it looks like this:
```
|--dashboard-auto_reload
    |--   auto_reload.py
    |--   chromedriver.exe
    |--   config.json
```
### How to use
To run the script simply start python and pass the script as a command line argument:
```
python auto_reload.py
```
