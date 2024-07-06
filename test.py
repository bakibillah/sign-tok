import requests

session = requests.session()

burp0_url = "https://www.tiktok.com:443/api/challenge/item_list/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.54&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&challengeID=13187&channel=tiktok_web&cookie_enabled=true&count=30&cursor=30&device_id=7195820289077478917&device_platform=web_pc&focus_state=true&from_page=hashtag&history_len=5&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=RO&root_referer=https%3A%2F%2Fwww.tiktok.com%2F404%3FfromUrl%3D%2Fhashtag&screen_height=1120&screen_width=1792&tz_name=Europe%2FBucharest&verifyFp=verify_ldo6d7go_rfalj7WR_Cqtf_4z9G_Aj1J_WSrSUzWZSJ6U&webcast_language=en&msToken=8G5wMuMotboG4hiWsuvDxdQ-VbOZh29r-tMYpFzA56ODNmsk1_RL6xYfiJJvzznY8jK4h4m9CHR2QHJLayqE7lzKFm97L5pmXen7VCGVVIt9s6vU2nNnlmiZW-HTn10YT83WW__OMEaK42s=&X-Bogus=DFSzswVOe5bANjvTS4iHxr7TlqCW&_signature=_02B4Z6wo0000146bL2gAAIDAGk10ZlbQ1n-OmyvAAICC3d"

burp0_headers = {"Accept": "application/json, text/plain, */*",
                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                 "X-Tt-Params": "mb+z3Pl1d/bc+N0SKnc7nTzeLcj4+pxPtoKlgh6xJXTzsUIV4QKk9beKXnLVWGL6aO/7HYJNO5yQ54Z+DdTPEAANyNJQhyl1ey2m++tnVZYZX4OfFphmFR4EJtl8eFknUTgvp40P1De8Vu3XUyxmzR/NWk7bnHRPVwFBTiPNVlcquP9tcAqOk9W/nxepBFp/gKPnYZXVZRmJAgKlVsn3ChDxXKIkNyFvOeOBONvIilEnTTvBF8YlWiSCYu6t7ONp85w8eSU0xm3j9TZz5iybocnpETriOJ6cgXL4b/1+aX0lMQsIgzc5CSs2AE9c6O21fsGt/ImeaZF7UzAsfWzRSfAxr6z97m5lrlzqCwjmf2602RXuimFpDjgi+nkJdzE6i8C1OCWLqneKmYKL5cWOhyWJJNLXBe5xCRM+daUDs4fcFVgofOCgA7JXQ2Dv9IzZ/xMMGh0yyoXOhMMjvCA4yA==", "Accept-Encoding": "gzip, deflate"}
res = session.get(burp0_url, headers=burp0_headers)
data = res.text

print(data)

