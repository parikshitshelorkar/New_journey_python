from concurrent.futures import ThreadPoolExecutor

def download(policy_id):
    print("Downloading policy", policy_id)
    return policy_id

policy_ids = [101, 102, 103, 104, 105]

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(download, policy_ids)

print(list(results))