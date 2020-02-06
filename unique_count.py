import pandas as pd
import glob

counties = glob.glob("exports/Detail/*.csv")

counts = pd.DataFrame(columns=['Name', 'Unique'])

for county in counties:
  data = pd.read_csv(county, low_memory=False)
  data['Residence Address Line 1'] = data['Residence Address Line 1'].str.lower()

  count = data['Residence Address Line 1'].nunique()
  counts = counts.append({'Name': county[15:18], 'Unique': count}, ignore_index=True)

counts.to_csv('house_count.csv')

print(counts)