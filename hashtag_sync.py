import asyncio
import json
import time

from playwright_stealth import stealth_sync
from playwright.sync_api import sync_playwright, Playwright


class HashtagSync:
    def __init__(self):
        self.proxy_local = {
            "server": "http://127.0.0.1:8000",
            "username": "",
            "password": ""
        }
        self.browser_args: list = [
            '--start-maximized',
            '--disable-dev-shm-usage',
            '--no-sandbox'
        ]
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, args=self.browser_args, proxy=self.proxy_local)
        self.page = self.browser.new_page()
        stealth_sync(self.page)
        self.page.on("response", lambda response: self.handle_response(response))

    def handle_response(self, response):
        try:
            print(response.url)
            if 'epsf.ticketmaster.com/eps-d?' in response.url:
                print(f"Received a response: {response.url} status code: {response.status} inside if")
                # text = await response.text()
                # print(f"Response url: {response.url} \n\n\ntext: \n\n{text}")
                # json_cookie = json.loads(text)
                # token_value = json_cookie['token']
                # print(token_value)
        except Exception as e:
            print(e)

    def run(self):
        self.page.goto("https://tiktok.com")

    def close(self):
        self.browser.close()


hashtag_search = HashtagSync()
hashtag_search.run()
time.sleep(60)
hashtag_search.close()
