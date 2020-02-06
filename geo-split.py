import json
import pandas as pd
from pandas.io.json import json_normalize

filename = "GEOJSON/state.geojson"

state = pd.read_json(path_or_buf=filename)

properties = json_normalize(state['properties'])

state = state.join(properties)

countylist = state.county.unique()
for county in countylist:
  source = state
  source = source.loc[source['county'] == county]
  source = source.drop(columns=["county", "countypct", "pct"])

  header = '{"type": "FeatureCollection", "name": "state", "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },"features": '
  footer = '}'

  geofile = "GEOJSON/counties/" + county + ".geojson"
  source.to_json(path_or_buf=geofile, orient='records')

  print("Generated " + geofile)

  with open(geofile, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header + content + footer)