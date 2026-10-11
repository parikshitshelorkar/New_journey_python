from pydantic import BaseModel, Field


class PolicyCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=5)
    maturity: str
    premium: float = Field(gt=0)


class PolicyUpdate(PolicyCreate):
    pass


class PolicyResponse(PolicyCreate):
    id: int

#
policies = [
    {
        "id": 1,
        "name": "Jeevan Labh",
        "description": "Life insurance savings plan",
        "maturity": "10 years",
        "premium": 15000.0
    }
]