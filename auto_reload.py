
import asyncio
import json
import signal
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

async def run():
    config = json.load(open('config.json'))
    url = config['url']
    email = config['user']['email']
    password = config['user']['password']

    while True:
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--incognito")
            options.add_argument("--start-fullscreen")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            driver = webdriver.Chrome(options=options)
            
            driver.get(url)

            WebDriverWait(driver, 20).until(
                lambda x: x.find_element(By.ID, 'username'))
            
            driver.find_element(By.ID, 'username').send_keys(email)
            driver.find_element(By.ID, 'password').send_keys(password)
            driver.find_element(By.ID, 'submit').click()

            await asyncio.sleep(config['reloadAfterSec'])
        except TimeoutException:
            await asyncio.sleep(10)
        finally:
            driver.quit()

class ExitOnInterrupt(SystemExit):
    code = 1

def exit_on_interrupt(*args):
    event_loop.stop()
    raise ExitOnInterrupt()

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    signal.signal(signal.SIGINT, exit_on_interrupt)
    signal.signal(signal.SIGTERM, exit_on_interrupt)

    try:
        event_loop.run_until_complete(run())
    except ExitOnInterrupt:
        pass
    finally:
        event_loop.close()
