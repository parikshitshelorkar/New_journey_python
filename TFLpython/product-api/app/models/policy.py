from dataclasses import dataclass


@dataclass
class Policy:
    id: int
    name: str
    description: str
    maturity: str
    premium: float

policy = Policy(id=1, name="Jeevan Labh", description="Life insurance savings plan", maturity="10 years",premium=15000.0)

print(policy.name)
print(policy.premium)