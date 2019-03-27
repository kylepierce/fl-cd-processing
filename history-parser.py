import pandas as pd

data = pd.read_csv('history.txt', sep="\t", header=None, low_memory=False)
data.columns = ["County Code", "Voter ID", "Election Date", "Election Type", "History Code"]
data.to_csv('history.csv', index=False)