import pandas as pd
# import numpy as np

# Simple classification
def classification(row):
  if row['voted16'] and row['voted18']:
    return "Hot"
  elif row['voted16'] or row['voted18']:
    return "Warm"
  else:
    return "Cold"

county = input("What County? ")

# Get voter details and clean
details = pd.read_csv('imports/Detail/' + county + '_20190312.txt', sep="\t", header=None, low_memory=False)
details.columns = ["County Code", "Voter ID", "Name Last", "Name Suffix", "Name First", "Name Middle", "Requested public records", "Residence Address Line 1", "Residence Address Line 2", "Residence City (USPS)", "Residence State", "Residence Zipcode", "Mailing Address Line 1", "Mailing Address Line 2", "Mailing Address Line", "Mailing City", "Mailing State", "Mailing Zipcode", "Mailing Country", "Gender", "Race", "Birth Date", "Registration Date", "Party Affiliation", "Precinct", "Precinct Group", "Precinct Split", "Precinct Suffix", "Voter Status", "Congressional District", "House District", "Senate District", "County Commission District", "School Board District", "Daytime Area Code ", "Daytime Phone Number", "Daytime Phone Extension", "Email address"]

details = details.drop(columns=["Congressional District", "House District", "Senate District", "County Commission District", "School Board District", "Daytime Area Code ", "Daytime Phone Number", "Daytime Phone Extension", "Email address"])

# Import the history
history = pd.read_csv('imports/History/' + county + '_H_20190312.txt', header=None, sep="\t", low_memory=False, names=["County Code", "Voter ID", "Election Date", "Election Type", "History Code"])

# Select only the essential info
details = details[['Voter ID', 'Precinct', 'Party Affiliation']]

# Remove 3rd party voters
details = details[details['Party Affiliation'].isin(["REP", "DEM", "NPA"])]

# Filter only the major elections
history = history[history['Election Date'].isin(["11/06/2012", "11/04/2014", "11/08/2016", "11/06/2018"])]

# Check if votes were for major elections
history['voted12'] = history['Election Date']=="11/06/2012"
history['voted14'] = history['Election Date']=="11/04/2014"
history['voted16'] = history['Election Date']=="11/08/2016"
history['voted18'] = history['Election Date']=="11/06/2018"

# Combine all of the votes by a single voter
history = history.groupby(['Voter ID']).sum()

# Detect what type of voter they are
history['status'] = history.apply(classification, axis=1)

# Remove boolean columns
history = history.drop(columns=["voted12", "voted14", "voted16", "voted18"])

# Join tables to get precinct and party info
voters = details.merge(history, left_on='Voter ID', right_on='Voter ID')

# Group the precinct, party and status.
precincts = voters.groupby(['Precinct', 'Party Affiliation', 'status']).count()

# Pandas throws an error on groupby since the indexes are missing. So reset the index.
precincts = precincts.reset_index()

# Make a wide format. Each precinct has its own line.
precincts = precincts.pivot_table(index='Precinct', columns=['Party Affiliation', 'status'], values='Voter ID')

# Export the final result
precincts.to_csv('exports/' + county + '.csv')