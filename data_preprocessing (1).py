import pandas as pd

# Load datasets
application_df = pd.read_csv("application_record.csv")
credit_df = pd.read_csv("credit_record.csv")

# Display first few rows
print(credit_df.head())

# Display unique STATUS values
print(credit_df["STATUS"].unique())

# Convert STATUS to binary
def to_binary(status):
    if status in ['0', 'X', 'C']:
        return 1
    else:
        return 0

# Apply the function
credit_df["STATUS_BIN"] = credit_df["STATUS"].apply(to_binary)

# Check the result
print(credit_df["STATUS_BIN"].value_counts())

# Merge the datasets
final_df = application_df.merge(
    credit_df,
    on="ID",
    how="left"
)

# Check merged dataset
print(final_df.shape)
print(final_df.head())

# Check missing values
print(final_df.isnull().sum())

# Save the merged dataset
final_df.to_csv("final_dataset.csv", index=False)

print("Final dataset created successfully!")
