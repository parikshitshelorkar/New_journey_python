import sys

policy = {
    "policy_id": "POL1001",
    "customer": "Ravi",
    "coverage": 1000000
}
# An object can have multiple references pointing to it.
print(sys.getrefcount(policy))
#getrefcount creates one reference for the object
