import requests
import argparse
import concurrent.futures
parser = argparse.ArgumentParser()
parser.add_argument("--d", required=True, help="The target domain")
parser.add_argument("--w", required=True, help="The target wordlist")
parser.add_argument('--threads', type=int,help='Number of threads', default=10)
args = parser.parse_args()
domain = args.d.replace("http://", "").replace("https://", "").strip("/")
wordlist = args.w
max_threads = args.threads
with open(wordlist) as file:
    subdomains = file.read().splitlines()
def check_subdomain(subdomain):
    url = f"https://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return f"[200 OK] {url}"
        elif response.status_code in (301, 302):
            return f"[Redirect {response.status_code}] {url}"
        elif response.status_code == 403:
            return f"[403 Forbidden] {url}"
        elif response.status_code == 404:
            return f"[404 Not Found] {url}"
        else:
            return f"[{response.status_code}] {url}"
    except requests.RequestException:
        return None
with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(check_subdomain,d)for d in subdomains]
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()

            if result:
                print(result)
        except Exception as e:
            print("Error",e)

