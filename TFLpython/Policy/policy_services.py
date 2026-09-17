import Policy.exceptions

class PolicyService:
    def create_policy(policy):
        if policy.premium <= 0:
            raise InvalidPremiumException(Exception)

    def calculate_premium(self, policy):
        return policy.premium

    def is_active(self, policy):
        return policy.premium > 0
    