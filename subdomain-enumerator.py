import requests # This modeule is to send requests to url
import argparse # Ye chu for taking input from use  . Highly flexible then arg.parse
import concurrent.futures # ye chu for threading
parser = argparse.ArgumentParser()
parser.add_argument("--d", required=True, help="The target domain")
parser.add_argument("--w", required=True, help="The target wordlist")
parser.add_argument('--threads', type=int,help='Number of threads', default=10)
args = parser.parse_args()
domain = args.d.replace("http://", "").replace("https://", "").strip("/")# ye chu incase user enters http:// . We remove it 
wordlist = args.w
max_threads = args.threads
with open(wordlist) as file: # We open the wordlist
    subdomains = file.read().splitlines() # Take all subdomain in wordlist
def check_subdomain(subdomain): #  Main function ju chu check kran all subdomains
    url = f"https://{subdomain}.{domain}" # ye chu url banawan jemis sozav es request
    try:
        response = requests.get(url, timeout=3) # sending actual requests
        if response.status_code == 200: #  Different codes we get we print
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
with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor: # Actual threads
    futures = [executor.submit(check_subdomain,d)for d in subdomains] # Loop through subdomains in worlist anf give them to main  function
    for future in concurrent.futures.as_completed(futures): # Check the completed threads and block code completion until all threads run
        try:
            result = future.result() # Store results and print if result does not have none

            if result:
                print(result)
        except Exception as e:
            print("Error",e)

