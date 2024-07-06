import random
import time
import requests
from requests import JSONDecodeError

session = requests.session()


class HashTagScraper:
    def __init__(self, challenge_name):
        self.signature_server_url: str = 'http://127.0.0.1:8888/signature'

        self.challenge_name: str = challenge_name
        self.challengeID: str = self.get_challenge_id(challenge_name)
        self.base_url: str

    def get_signature(self, cursor):
        headers_ = {
            'Content-type': 'application/json',
        }

        input_url_hashtag = f'https://www.tiktok.com/api/challenge/item_list/?aid=1988&count=30&challengeID={self.challengeID}&cursor={cursor}&cookie_enabled=true&screen_width=0&screen_height=0&browser_language=&browser_platform=&browser_name=&browser_version=&browser_online=&timezone_name=Europe%2FLondon'
        input_url_search = f'https://www.tiktok.com/api/search/general/full/?aid=1988&offset=0&keyword=princemamun&cookie_enabled=true&screen_width=0&screen_height=0&browser_language=&browser_platform=&browser_name=&browser_version=&browser_online=&timezone_name=Europe%2FLondon'

        response = requests.post(self.signature_server_url, headers=headers_, data=input_url_hashtag)

        x_tt_params = response.json()['data']['x-tt-params']
        return x_tt_params

    def get_hashtag_data(self, number_of_page):
        for index in range(number_of_page):
            url = f"https://www.tiktok.com:443/api/challenge/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.54&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&challengeID=13187&channel=tiktok_web&cookie_enabled=true&count=30&cursor=30&device_id=7195820289077478917&device_platform=web_pc&focus_state=true&from_page=hashtag&history_len=5&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=RO&root_referer=https%3A%2F%2Fwww.tiktok.com%2F404%3FfromUrl%3D%2Fhashtag&screen_height=1120&screen_width=1792&tz_name=Europe%2FBucharest&verifyFp=verify_ldo6d7go_rfalj7WR_Cqtf_4z9G_Aj1J_WSrSUzWZSJ6U&webcast_language=en&msToken=8G5wMuMotboG4hiWsuvDxdQ-VbOZh29r-tMYpFzA56ODNmsk1_RL6xYfiJJvzznY8jK4h4m9CHR2QHJLayqE7lzKFm97L5pmXen7VCGVVIt9s6vU2nNnlmiZW-HTn10YT83WW__OMEaK42s=&X-Bogus=DFSzswVOe5bANjvTS4iHxr7TlqCW&_signature="
            url_search = f"https://www.tiktok.com:443/api/search/general/full/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.54&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&keyword=princemamun&channel=tiktok_web&cookie_enabled=true&offset=0&device_id=7195820289077478917&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=RO&root_referer=https%3A%2F%2Fwww.tiktok.com%2F404%3FfromUrl%3D%2Fhashtag&screen_height=1120&screen_width=1792&tz_name=Europe%2FBucharest&verifyFp=verify_ldo6d7go_rfalj7WR_Cqtf_4z9G_Aj1J_WSrSUzWZSJ6U&webcast_language=en&msToken=8G5wMuMotboG4hiWsuvDxdQ-VbOZh29r-tMYpFzA56ODNmsk1_RL6xYfiJJvzznY8jK4h4m9CHR2QHJLayqE7lzKFm97L5pmXen7VCGVVIt9s6vU2nNnlmiZW-HTn10YT83WW__OMEaK42s=&X-Bogus=DFSzswVOe5bANjvTS4iHxr7TlqCW&_signature=_02B4Z6wo0000146bL2gAAIDAGk10ZlbQ1n-OmyvAAICC3d"
            headers = {"Accept": "application/json, text/plain, */*",
                       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                       "X-Tt-Params": self.get_signature(index),
                       "Accept-Encoding": "gzip, deflate"
                       }
            res = session.get(url, headers=headers)
            try:
                data = res.json()

                cursor_static = data['cursor']
                has_more = data['hasMore']
                if has_more is False:
                    print("no more page is available, so exiting the scraper")
                    break
                itemList = data['itemList']

                print(f"itemList: found {len(itemList)} items")
                for item in itemList:
                    try:
                        description = item['contents'][0]['desc']
                        # print(f"{index + 1}: {description}")
                    except KeyError:
                        pass


                time.sleep(random.randint(3, 5))
            except JSONDecodeError:
                time.sleep(5)
                print(f"json decode error: {index+1}")

    def get_challenge_id(self, challenge_name):
        cookies = {
            'tt_chain_token': 'Q0xv58vEGZHRpyWqjKUxeA==',
            'odin_tt': 'f0cea1ccb5856617996265983a9dcd3ded1ff49c0725166b2d7e55af0e5aff56007c0b7ba2457c36f87a7da97a066adb72f5f67f4c9f88779a02249ff6c65f4281b42360e9bedd6f21aa61a89ddf356f',
            'passport_csrf_token': 'fcea2f4b873a2f14239abd68028509b8',
            'passport_csrf_token_default': 'fcea2f4b873a2f14239abd68028509b8',
            'ttwid': '1%7CFI84eJ_pEU-KH6dFzAoYmPzB-bLrktMejmVKQmwZjyo%7C1710411981%7C5043521b903b5a0945d1fa37cbfd17e22d1fa33e58f3b9fdf20e985011b6506d',
            'msToken': 'n5ADBO9EEFV4-kWxqwEuM8ejlvQ3AzPsHgzNt7OlQydsGBDrAQFuWHm43mjGElMDDuoHPIsYMz4tdUUD8xoMfNOL_9rjWuSv3Y6NEMpGEDvQDpg7Mv0C5SYYpSoYmtRgiEVvdA==',
            '_ttp': '2dgDseMhimRWvtvrMBR2Cy4GnA0',
        }

        headers_challenge = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7,it;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://github.com/carcabot/tiktok-signature/issues/181',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

        params = {
            'challengeName': challenge_name,
        }

        response = requests.get('https://t.tiktok.com/api/challenge/detail/', params=params, cookies=cookies, headers=headers_challenge)

        self.challengeID = response.json()["challengeInfo"]["challenge"]["id"]

        print(f"Challenge ID: {self.challengeID} for {challenge_name}")
        return self.challengeID


scraper_instance = HashTagScraper('tiktokbangladesh')
scraper_instance.get_hashtag_data(1000)
