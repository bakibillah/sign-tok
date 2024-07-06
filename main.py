import json
import random
import requests
import string
import os.path
from Naked.toolshed.shell import muterun_js

referer = "https://www.tiktok.com/"
url = "https://www.tiktok.com/api/challenge/item_list/?aid=1988&count=30&challengeID=1624626732781573&cursor=0&cookie_enabled=true&screen_width=0&screen_height=0&browser_language=&browser_platform=&browser_name=&browser_version=&browser_online=&timezone_name=Europe%2FLondon"

response = muterun_js(' '.join(['/home/baki/WebstormProjects/tiktok-signature/browser.js', "\""+url+"\""]))
# print(response.stdout)
if response.exitcode == 0:
    # the command was successful, handle the standard output
    stdout_str = response.stdout
    data_str = stdout_str.decode().strip()

    # Split the data string by newline characters to separate the JSON part
    json_str = data_str.split('\n')[-1]
    signature = json.loads(json_str)
#     print(signature)
#     request = requests.get(signature['data']['signed_url'], headers={"method": "GET",
#                                                                      "accept-encoding": "gzip, deflate",
#                                                                      "Referer": referer,
#                                                                      "user-agent": signature['data']['navigator']['user_agent'],
#                                                                      "x-tt-params": signature['data']['x-tt-params']
#                                                                      })

    # data = request.text
    import requests

    session = requests.session()
    x_tt_params = signature['data']['x-tt-params']
    url = "https://www.tiktok.com:443/api/challenge/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.54&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&challengeID=13187&channel=tiktok_web&cookie_enabled=true&count=30&cursor=30&device_id=7195820289077478917&device_platform=web_pc&focus_state=true&from_page=hashtag&history_len=5&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=RO&root_referer=https%3A%2F%2Fwww.tiktok.com%2F404%3FfromUrl%3D%2Fhashtag&screen_height=1120&screen_width=1792&tz_name=Europe%2FBucharest&verifyFp=verify_ldo6d7go_rfalj7WR_Cqtf_4z9G_Aj1J_WSrSUzWZSJ6U&webcast_language=en&msToken=8G5wMuMotboG4hiWsuvDxdQ-VbOZh29r-tMYpFzA56ODNmsk1_RL6xYfiJJvzznY8jK4h4m9CHR2QHJLayqE7lzKFm97L5pmXen7VCGVVIt9s6vU2nNnlmiZW-HTn10YT83WW__OMEaK42s=&X-Bogus=DFSzswVOe5bANjvTS4iHxr7TlqCW&_signature=_02B4Z6wo0000146bL2gAAIDAGk10ZlbQ1n-OmyvAAICC3d"
    headers = {"Accept": "application/json, text/plain, */*",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
               "X-Tt-Params": x_tt_params, "Accept-Encoding": "gzip, deflate"}
    res = session.get(url, headers=headers)

    data2 = res.json()

    print(data2)

else:
    standard_err = response.stderr
    exit_code = response.exitcode
    print('Cannot run node script ' + str(exit_code) + ': ' + standard_err)
