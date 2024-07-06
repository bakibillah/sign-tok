import requests

burp0_url = "https://www.tiktok.com/api/challenge/item_list/?WebIdLastTime=1710402923&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-GB&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F122.0.0.0%20Safari%2F537.36&challengeID=1660738704663553&channel=tiktok_web&cookie_enabled=true&count=30&coverFormat=2&cursor=0&device_id=7346124544983188993&device_platform=web_pc&focus_state=true&from_page=hashtag&history_len=3&is_fullscreen=false&is_page_visible=true&language=en&odinId=7346122512781493249&os=linux&priority_region=&referer=&region=BD&screen_height=1080&screen_width=1920&tz_name=Asia%2FDhaka&webcast_language=en&msToken=Bd5xGpWVdxswKnSEVtavd6H5i5cqYUCKCfnNj1OY6z6Qf5WAw48xkOZtj24mquv_gTLFS4KAFibZ-F6dOUOxR07zNoQAZmQVsMUAaaGS3Py24iCC-qflrSL8ABl7TGwZUHW8vA=="


def get_signature(cursor, challengeID):
    headers_ = {
        'Content-type': 'application/json',
    }

    input_url_hashtag = f'https://www.tiktok.com/api/challenge/item_list/?aid=1988&count=30&challengeID={challengeID}&cursor={cursor}&cookie_enabled=true&screen_width=0&screen_height=0&browser_language=&browser_platform=&browser_name=&browser_version=&browser_online=&timezone_name=Europe%2FLondon'
    input_url_search = f'https://www.tiktok.com/api/search/general/full/?aid=1988&offset=0&keyword=princemamun&cookie_enabled=true&screen_width=0&screen_height=0&browser_language=&browser_platform=&browser_name=&browser_version=&browser_online=&timezone_name=Europe%2FLondon'

    response = requests.post("http://127.0.0.1:8888/signature", headers=headers_, data=burp0_url)

    x_tt_params = response.json()['data']
    return x_tt_params


xttparams = get_signature(cursor=0, challengeID=1660738704663553, )

signature = xttparams['signature']
verify_fp = xttparams['verify_fp']
xbogus= xttparams['x-bogus']
signed_url = xttparams['signed_url']

print(signature)
print(verify_fp)
print(xbogus)
print(signed_url)
