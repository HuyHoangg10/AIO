import pandas as pd

DATASET_PATH = "./Pokemon.csv"
data = pd.read_csv(DATASET_PATH)

# Save DataFrame to CSV separated by tab (optional)
# data.to_csv("dragon_ball.csv", sep='\t')

# Display the first few rows (optional)
# data_top = data.head(10)
# print(data_top)

# Drop the original 'Total' column
data = data.drop(columns="Total")

# Re-create the 'Total' column by calculating the sum of stats (appended at the end)
data["Total"] = data["Attack"] + data["Defense"] + data["HP"]

# Re-fetch updated column names AFTER adding the new column
# At this point, col[-1] correctly references the newly created 'Total' column
col = list(data.columns.values)

# Reorder columns: place 'Total' (col[-1]) right after 'Name' (col[0:2])
data = data[col[0:2] + [col[-1]] + col[2:-1]]

# Configure display options to show all columns without truncation ('...')
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

#select row by iloc
# print(data.iloc[3:9])

#select row by condition
# print(data.loc[data["Legendary"]==True].head(5))


# Inspect DataFrame metadata, including column data types, non-null counts, and memory usage
# print(data.info())

# Generate descriptive summary statistics (mean, std, quartiles, min, max) for numerical columns
# print(data.describe())

#sorting 
# print(data.sort_values("Type 2").head(5).reset_index(drop=True))

#groupby
print(data.groupby("Type 1").mean(numeric_only=True).sort_values("Attack",ascending=False).head(15))