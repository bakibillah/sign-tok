import asyncio
import dataclasses
import json
import random
import time
from typing import Any
from hashtag import Hashtag
from playwright_stealth import stealth_async
from playwright.sync_api import sync_playwright, Playwright
from playwright.async_api import async_playwright, Playwright


@dataclasses.dataclass
class TikTokPlaywrightSession:
    """A TikTok session using Playwright"""

    context: Any
    page: Any
    proxy: str = None
    params: dict = None
    headers: dict = None
    ms_token: str = None
    base_url: str = "https://www.tiktok.com"


class HashtagaSync:
    hashtag = Hashtag

    def __init__(self):
        self.headers = dict()
        self.params = dict()
        self.page = None
        self.browser = None
        self.playwright = None
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

    async def __set_session_params(self, session: TikTokPlaywrightSession):
        """Set the session params for a TikTokPlaywrightSession"""
        user_agent = await session.page.evaluate("() => navigator.userAgent")
        language = await session.page.evaluate(
            "() => navigator.language || navigator.userLanguage"
        )
        platform = await session.page.evaluate("() => navigator.platform")
        device_id = str(random.randint(10 ** 18, 10 ** 19 - 1))  # Random device id
        history_len = str(random.randint(1, 10))  # Random history length
        screen_height = str(random.randint(600, 1080))  # Random screen height
        screen_width = str(random.randint(800, 1920))  # Random screen width
        timezone = await session.page.evaluate(
            "() => Intl.DateTimeFormat().resolvedOptions().timeZone"
        )

        session_params = {
            "aid": "1988",
            "app_language": language,
            "app_name": "tiktok_web",
            "browser_language": language,
            "browser_name": "Mozilla",
            "browser_online": "true",
            "browser_platform": platform,
            "browser_version": user_agent,
            "channel": "tiktok_web",
            "cookie_enabled": "true",
            "device_id": device_id,
            "device_platform": "web_pc",
            "focus_state": "true",
            "from_page": "user",
            "history_len": history_len,
            "is_fullscreen": "false",
            "is_page_visible": "true",
            "language": language,
            "os": platform,
            "priority_region": "",
            "referer": "",
            "region": "US",  # TODO: TikTokAPI option
            "screen_height": screen_height,
            "screen_width": screen_width,
            "tz_name": timezone,
            "webcast_language": language,
        }
        self.params = session_params

    async def create_playwright_instance(self):
        self.playwright = await async_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, args=self.browser_args, proxy=self.proxy_local)
        request_headers = None

    def handle_request(self, request):
        self.headers = request.headers

    async def handle_response(self, response):
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

    async def create_playwright_session(self, context_options: dict = {}, ms_token: str = None, ):
        context = await self.browser.new_context(proxy=self.proxy_local, **context_options)

        page = await context.new_page()
        await stealth_async(page)
        page.once("request", self.handle_request)
        await page.on("response", lambda response: self.handle_response(response))
        await page.goto("https://tiktok.com")

        session = TikTokPlaywrightSession(
            context,
            page,
            ms_token=ms_token,
            headers=self.headers,
            base_url="https://tiktok.com",
        )
        await self.__set_session_params(session)

    def close(self):
        self.browser.close()


# hashtag_search = HashtagSync()
# hashtag_search.run()
# time.sleep(60)
# hashtag_search.close()
async def get_hashtag_videos():
    async with HashtagaSync() as api:
        await api.create_playwright_instance()
        await api.create_playwright_session()
        tag = api.hashtag(name="funny")
        async for video in tag.videos(count=30):
            print(video)

        api.close()


if __name__ == "__main__":
    asyncio.run(get_hashtag_videos())
