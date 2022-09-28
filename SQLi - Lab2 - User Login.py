from ssl import VerifyFlags
import sys
import requests
import urllib3
import urllib

# Disables warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Setting up the proxies
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080', VerifyFlags=False}

def attemptLogin(url):
    print(url)
    
def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Enumerating the web page...")
    attemptLogin(url)

if __name__ == "__main__":
    main()