import pandas as pd
import glob, os

for subdir, dirs, files in os.walk('./imports/History'):
  for filename in files:
    # Get voter details and clean
    details = pd.read_csv('imports/History/' + filename, sep="\t", header=None, low_memory=False)
    details.columns = ["County Code", "Voter ID", "Election Date", "Election Type", "History Code"]    
    county = filename[0:3]
    print(county)
    details.to_csv('exports/History/' + county + '20190312.csv', index=False)
