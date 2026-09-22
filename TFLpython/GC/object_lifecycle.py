class Customer:
    pass

class InsurancePolicy:
    pass

customer = Customer()
policy = InsurancePolicy()

customer.policy = policy
policy.customer = customer

# remove external reference
del customer
del policy

import gc
print(gc.collect())