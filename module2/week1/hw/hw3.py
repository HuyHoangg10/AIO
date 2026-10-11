import pandas as pd
import numpy as np

df = pd.read_csv("./advertising.csv")

data = df.to_numpy()
print(df)

sale_columns = data[:, 3]
# max_sale = np.max(sale_columns)
# index_sale = np.argmax(sale_columns)
# print(f"index: {index_sale} max_value: {max_sale}")

# sale_greater_than_20 = np.array(sale_columns>=20)
# sale_value_gt20 = sale_columns[sale_greater_than_20]
# print(sale_value_gt20.size)

# tv_columns = data[:,0]
# mean_tv_col = np.mean(tv_columns)
# print(mean_tv_col)

# radio_col = data[:,1]
# radio_mean_value = np.mean(radio_col[sale_columns>=15])
# print(radio_mean_value)

# news_col = data[:,2]
# new_mean = np.mean(news_col)
# total_sale_value = np.sum(sale_columns[news_col>new_mean])
# print(total_sale_value)

mean_sale_value = np.mean(sale_columns)
score = np.array(["Good","Average","Bad"])
score = np.where(sale_columns == mean_sale_value,score[1],np.where(sale_columns > mean_sale_value,score[0],score[2]))
print(score[7:10])

arg_min_sale_minus_mean = np.argmin(np.abs(sale_columns - mean_sale_value))
min_sale_minus_mean = sale_columns[arg_min_sale_minus_mean]
score1 = np.array(["Good","Average","Bad"])
score1 = np.where(sale_columns == min_sale_minus_mean,score[1],np.where(sale_columns > min_sale_minus_mean,score[0],score[2]))
print(score1[7:10])