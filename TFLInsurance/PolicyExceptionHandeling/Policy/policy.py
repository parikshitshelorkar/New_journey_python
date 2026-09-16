from .exceptions import (
    PolicyNotFoundException,
    InvalidPremiumException,
    PolicyExpiredException
)

class Policy:

    policies = {}

    def __init__(
        self,
        policy_number,
        customer_id,
        policy_type,
        premium
    ):
        self.policy_number = policy_number
        self.customer_id = customer_id
        self.policy_type = policy_type
        self.premium = premium


    @classmethod
    def create_policy(cls, policy_number, customer_id, premium):
        if premium < 0:
            raise InvalidPremiumException(
                "Premium must be greater than zero"
            )
        policy = cls(policy_number, customer_id, "Active", premium)
        cls.policies[policy_number] = policy

        return policy

    @classmethod
    def find_policy(cls, policy_number):
        if policy_number not in cls.policies:
            raise PolicyNotFoundException(
                "Policy not found"
            )
        return cls.policies[policy_number]

    @classmethod
    def pay_premium(cls, policy_number, amount):
        policy = cls.find_policy(policy_number)
        if policy.policy_type == "Expired":
            raise PolicyExpiredException(
                "Cannot pay premium for expired policy"
            )
        policy.premium += amount
    