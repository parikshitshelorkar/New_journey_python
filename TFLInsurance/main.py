import Policy

p = Policy("POL101", "Parikshit", 5000, "Active")

print(p.policy_number)
print(p.customer_name)
print(p.premium)
print(p.status)

policies = {p}