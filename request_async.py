import asyncio
import time
import os
import aiohttp
import aiofiles
from aiohttp import *
from events import url_list


async def fetch(session, url, count, reese84, user_agent):
    proxy_url = "http://brd-customer-hl_1996909c-zone-pm_rotate-country-usujz9dzsq3as1@brd.superproxy.io:22225"

    cookies = {"eps_sid": "",
               "pxcts": "",
               "_pxvid": "",
               "reese84": reese84
               }
    headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
               "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1",
               "User-Agent": user_agent,
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
               "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Dest": "document",
               "Referer": url,
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}

    async with session.get(url, headers=headers, cookies=cookies) as response:
    # async with session.get(url, headers=headers, cookies=cookies, proxy=proxy_url) as response:
        data = response.status
        print(f"{count}-{data}")
        if response.status == 200:
            html_content = await response.text()
            async with aiofiles.open(f'html_files/output-{count}.html', mode='w', encoding='utf-8') as file:
                await file.write(html_content)
            print(f'{count} - HTML content saved successfully.')
        else:
            print(f'Failed to retrieve content. Status code: {response.status}')


async def main_request(token_value, user_agent):

    reese84 = token_value
    output_directory = "html_files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for count, url in enumerate(url_list, 1):
            task = fetch(session, url, count, reese84, user_agent)
            tasks.append(task)

        await asyncio.gather(*tasks)
