import pandas as pd

data = pd.read_csv('importst/PAL_20190312.txt', sep="\t", header=None, low_memory=False)
data.columns = ["County Code", "Voter ID", "Name Last", "Name Suffix", "Name First", "Name Middle", "Requested public records", "Residence Address Line 1", "Residence Address Line 2", "Residence City (USPS)", "Residence State", "Residence Zipcode", "Mailing Address Line 1", "Mailing Address Line 2", "Mailing Address Line", "Mailing City", "Mailing State", "Mailing Zipcode", "Mailing Country", "Gender", "Race", "Birth Date", "Registration Date", "Party Affiliation", "Precinct", "Precinct Group", "Precinct Split", "Precinct Suffix", "Voter Status", "Congressional District", "House District", "Senate District", "County Commission District", "School Board District", "Daytime Area Code ", "Daytime Phone Number", "Daytime Phone Extension", "Email address"]

data = data.drop(columns=["Congressional District", "House District", "Senate District", "County Commission District", "School Board District", "Daytime Area Code ", "Daytime Phone Number", "Daytime Phone Extension", "Email address"])

data.to_csv('exports/details.csv')