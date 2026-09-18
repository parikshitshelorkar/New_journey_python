import json
import policy_repository

########## Generalize code ###############
with open ("policies.json", "r") as file:
    policies = json.load(file)
    
print(policies)

# with open("policies.json", "w") as file:
#     json.dump(policy, file, indent=4)

with open("policies.json", "r") as file:
    policies = json.load(file)

    new_policy = {
        "policy_number": "POL1003",
        "customer_name": "Amit",
        "premium": 18000,
        "status": "Active"
    }

policies.append(new_policy)

with open("policies.json", "w") as file:
    json.dump(policies, file, indent=4)

print(policies)

def find_policy(policy_number):
    with open("policies", "r") as file:
        policies.json.load(file)
    for policy in policies:
        if policy.policy_number == policy_number:
            print(policy)
    return None

policy = find_policy("POL1001")
print(policy)
#exception handeling
try:

    with open("policies.json", "r") as file:
        policies = json.load(file)

except FileNotFoundError:

    print("Policy file does not exist.")
    policies = []

except json.JSONDecodeError:
    print("Policy file contains invalid JSON.")
    policies = []


############ Modular code separating policy_repository ###########
repository = policy_repository.PolicyRepository("policies.json")
policies = repository.get_all()
print(policies)