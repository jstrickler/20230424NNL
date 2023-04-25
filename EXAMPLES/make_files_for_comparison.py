import pandas as pd

df = pd.read_csv("../DATA/city-of-chicago-salaries.csv")

df.to_pickle('../DATA/city-of-chicago-salaries.pic')

