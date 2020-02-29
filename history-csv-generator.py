import pandas as pd
import glob, os
import boto3

s3 = boto3.resource('s3')

import_dir = 'imports/History/'
date_folder = 'year=2020/month=2/'

for subdir, dirs, files in os.walk('./' + import_dir + date_folder):
  for filename in files:
    # Get voter details and clean
    details = pd.read_csv( import_dir + date_folder + filename, sep="\t", header=None, low_memory=False)
    details.columns = ["County Code", "Voter ID", "Election Date", "Election Type", "History Code"]    
    county = filename[0:3]
    print(county)

    directory = "exports/History/" + date_folder
    if not os.path.exists(directory):
      os.makedirs(directory)

    details.to_csv(directory + county + '.csv', sep='\t', index=False)
    
    #Upload to S3
    s3.meta.client.upload_file(directory + county + '.csv', 'fldemdatalake', 'CSV/History/' + date_folder + county + '.csv')