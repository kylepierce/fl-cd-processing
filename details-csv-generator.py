# import pandas as pd
import modin.pandas as pd
import glob, os

import_dir = 'imports/Detail/year=2020/month=1'

for subdir, dirs, files in os.walk('./' + import_dir):
  for filename in files:
    # Get voter details and clean
    details = pd.read_csv( import_dir + filename, sep="\t", header=None, low_memory=False)
    details.columns = ["County Code", "Voter ID", "Name Last", "Name Suffix", "Name First", "Name Middle", "Requested public records", "Residence Address Line 1", "Residence Address Line 2", "Residence City (USPS)", "Residence State", "Residence Zipcode", "Mailing Address Line 1", "Mailing Address Line 2", "Mailing Address Line", "Mailing City", "Mailing State", "Mailing Zipcode", "Mailing Country", "Gender", "Race", "Birth Date", "Registration Date", "Party Affiliation", "Precinct", "Precinct Group", "Precinct Split", "Precinct Suffix", "Voter Status", "Congressional District", "House District", "Senate District", "County Commission District", "School Board District", "Daytime Area Code ", "Daytime Phone Number", "Daytime Phone Extension", "Email address"]

    # mailer = details.copy()
    # mailer = mailer[["County Code", "Voter ID", "Mailing Address Line 1", "Mailing Address Line 2", "Mailing Address Line", "Mailing City", "Mailing State", "Mailing Zipcode", "Mailing Country"]]

    # details = details[["County Code", "Voter ID", "Name Last", "Name Suffix", "Name First", "Name Middle", "Requested public records", "Residence Address Line 1", "Residence Address Line 2", "Residence City (USPS)", "Residence State", "Residence Zipcode", "Gender", "Race", "Birth Date", "Registration Date", "Party Affiliation", "Precinct", "Precinct Group", "Precinct Split", "Precinct Suffix", "Voter Status", "Congressional District", "House District", "Senate District", "County Commission District", "School Board District", "Daytime Area Code ", "Daytime Phone Number", "Daytime Phone Extension", "Email address"]]
    
    county = filename[0:3]
    print(county)

    directory = "exports/Detail/county=" + county + "/year=2020/month=1/"
    if not os.path.exists(directory):
      os.makedirs(directory)

    details.to_csv(directory + county + '.csv', sep='\t', index=False)
