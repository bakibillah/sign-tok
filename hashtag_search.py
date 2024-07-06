import asyncio
import json
import time
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import datetime
from request_async import main_request


proxy = {
    "server": "http://brd.superproxy.io:22225",
    "username": "brd-customer-hl_1996909c-zone-pm_rotate-country-us",
    "password": "ujz9dzsq3as1"
}


proxy_local = {
    "server": "http://127.0.0.1:8080",
    "username": "",
    "password": ""
}


async def handle_response(response):
    print(f" Received a response: {response.url} status code: {response.status} inside if")
    try:
        if 'epsf.ticketmaster.com/eps-d?' in response.url:
            print(f" Received a response: {response.url} status code: {response.status} inside if")
            text = await response.text()
            print(f"Response url: {response.url} \n\n\ntext: \n\n{text}")
    except Exception as e:
        print(e)

try:
    async def run_browser_instance(url, n):
        async with async_playwright() as p:
            try:
                # browser = await p.chromium.launch(headless=False)
                browser = await p.chromium.launch(headless=False, proxy=proxy_local)
                context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
                page = await context.new_page()
                # page.set_default_timeout(120000)
                await stealth_async(page)
                # page.on('response', lambda response: handle_response(response))

                await page.goto(url)
                async with page.expect_response("https://example.com/resource") as response_info:
                    await page.get_by_text("trigger response").click()
                response = await response_info.value
                return response.ok
                # await page.wait_for_load_state("domcontentloaded")
                # page.on("response", lambda response: print(f"{n}: ", response.status, response.url, response.body, response.header) if response.url == url else None)
                # await page.screenshot(path=f"screenshot-{n}.png")
            except Exception as e2:
                print(e2)
except Exception as e:
    print(e)


async def main():
    tasks = []
    url = "https://tiktok.com"
    # for n, url in enumerate(url_list, start=1):
    #     task = run_browser_instance(url, n)
    #     tasks.append(task)
    await run_browser_instance(url)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
