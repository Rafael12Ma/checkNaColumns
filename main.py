import pandas as pd
df = pd.read_csv("C:/kl_csv/Classification/features_age.csv")
# Check for columns where all values are NaN
all_nan_columns = df.columns[df.isna().all()]

if len(all_nan_columns) > 0:
    print("Columns with all NaN values:")
    print(all_nan_columns)
else:
    print("No columns with all NaN values found.")
