class PolicyService:

    def calculate_premium(self, policy):
        return policy.premium

    def is_active(self, policy):
        return policy.premium > 0