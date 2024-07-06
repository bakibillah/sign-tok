from base64 import b64decode, b64encode
from urllib.parse import parse_qsl, urlencode

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(r):
    s = urlencode(r, doseq=True, quote_via=lambda s, *_: s)
    key = "webapp1.0+202106".encode("utf-8")
    cipher = AES.new(key, AES.MODE_CBC, key)
    ct_bytes = cipher.encrypt(pad(s.encode("utf-8"), AES.block_size))
    return b64encode(ct_bytes).decode("utf-8")


def decrypt(s):
    key = "webapp1.0+202106".encode("utf-8")
    cipher = AES.new(key, AES.MODE_CBC, key)
    ct = b64decode(s)
    s = unpad(cipher.decrypt(ct), AES.block_size)
    return dict(parse_qsl(s.decode("utf-8"), keep_blank_values=True))

from pprint import pprint
# xttparams = "mb+z3Pl1d/bc+N0SKnc7nU+E457oN7icLUsiou1JRQmiEyHAhSQQXcpha7FcPeHilaDld0N8iyL+Y8s0LsNmY6Tg/rRP4EfVlzSbcNKuVwY1Gcznw65BFmCkY576JfB/TrRYYLcSSAJoVicaLlbSyMz3+zrvBbU/AglxcrD9ddjS2VhS47QS/1TO5N3A1AKSCyG/Rk6ayDmeXFfFmlCqDhdbNmFAacVy6P2FxuZ4WSG7p4FgrK3jV/vEYjHqb1SxkUWyfGqkFFroa7MxijytsuNyL/hp36uoVgpEP0A11dB1M+emji133Z3Dg3zyjpc7TBi7IjEFAbtX5iXwOda2FqGoQOpPujBVpsvdvso3ANoV+e97OVf/yLL4qmvEqi6LA1zG03nUm/FwENgGdTJmekJdLrNYz3nAHN9Q9SaDSyIPlHIfDXuuZEdxk0HZibaJGe4XfFP0wgR3aMfaf7zFFg=="

# xttparams = decrypt(xttparams)

payload = {'aid': '1988', 'count': '30', 'challengeID': '1594201347146754', 'cursor': '0', 'cookie_enabled': 'true', 'screen_width': '0', 'screen_height': '0', 'browser_language': '', 'browser_platform': '',
           'browser_name': '', 'browser_version': '', 'browser_online': '', 'timezone_name': 'Europe/London',
           'verifyFp': 'verify_5b161567bda98b6a50c0414d99909d4b',
           '_signature': '_02B4Z6wo00f01Rfi9oQAAIBBUZQTHcyptgEX8vIAACAE9f', 'is_encryption': '1'}

xttparams = encrypt(payload)

print(xttparams)
