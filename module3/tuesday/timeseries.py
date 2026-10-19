import pandas as pd

DATASET_PATH = "./timeseries_daily-minimum-temperatures.csv"
data = pd.read_csv(DATASET_PATH) 

data["Date"] = pd.to_datetime(data["Date"])
data = data.set_index("Date")
print(data)

data["Daily minimum temperatures"] = pd.to_numeric(data["Daily minimum temperatures"],errors="coerce")

#time base indexing
#data frame plot