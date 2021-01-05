import requests
import json
import time

token = "token here..."

url = "https://discordapp.com/api/v6/users/@me/settings"

s = "insert text here..."

headers = {
    "Authorization": "{}".format(token),
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.9 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36",
    "Accept": "*/*",
    "Authority": "discordapp.com",
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "Host": "discordapp.com",
    "Connection": "keep-alive",
}

while True:
	data = {
		"custom_status": {
			"text": "{}".format(s)
		}
	}

	r = requests.request("PATCH", url, headers = headers, data = json.dumps(data))
	s = s[1:] + s[0]
	time.sleep(1)
