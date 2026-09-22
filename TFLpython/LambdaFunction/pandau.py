import pandas as pd

data = {
    "PolicyID": ["POL1001","POL1002","POL1003","POL1004","POL1005" ],
    "Customer": ["Ravi","Amit","Sneha","Priya","Rahul"],
    "Product": ["Life Protection", "Child Future", "Life Protection", "Retirement","Child Future"],
    "Premium": [25000,40000,15000,60000,30000],
    "Coverage": [1000000,2000000,500000,3000000,1500000],
    "Status": ["Active", "Active", "Inactive", "Active", "Active"]
}

df = pd.DataFrame(data)
print("#########################")
print(df)

#filtering
high_coverage = df[
    df["Coverage"].apply(
        lambda coverage: coverage > 1000000
    )
]
print()
print("#########################")
print(high_coverage)

#apply 10% discount to every premium
df["DiscountedPremium"] = df["Premium"].apply(
    lambda premium: premium * 0.90
)
print()
print("#########################")
print(df)

#Show policies with the highest premium first.
sorted_df = df.sort_values(
    by="Premium",
    ascending=False
)
print()
print("#########################")
print(sorted_df)

#If we specifically want to demonstrate a lambda as a sorting key:
sorted_df = df.sort_values(
    by="Premium",
    key=lambda column: column,
    ascending=False
)
print(sorted_df)

