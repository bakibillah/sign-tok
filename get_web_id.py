import requests

session = requests.session()

burp0_url = "https://mcs-sg.tiktok.com:443/v1/user/webid"
burp0_headers = {"Sec-Ch-Ua": "\"Not(A:Brand\";v=\"24\", \"Chromium\";v=\"122\"", "Sec-Ch-Ua-Platform": "\"Linux\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36", "Content-Type": "application/json", "Accept": "*/*", "Origin": "https://www.tiktok.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.tiktok.com/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=1, i", "Connection": "close"}
burp0_json={"app_id": 2740, "referer": "", "url": "https://www.tiktok.com/tag/viralvideo", "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36", "user_unique_id": ""}
session.post(burp0_url, headers=burp0_headers, json=burp0_json)
