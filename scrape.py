# Width – 225, Aspect Ratio – 50, Rim Size - 16

import re
import json
import requests
import pandas as pd


url = "http://www.dexel.co.uk/shopping/tyre-results?width=225&profile=50&rim=16&speed="

data = json.loads(
    re.search(r"allTyres = (.*);", requests.get(url).text).group(1)
)

# uncomment to print all data:
# print(json.dumps(data, indent=4))

df = pd.DataFrame(data)
print(df.head())

df = df[["manufacturer", "description", "winter", "summer", "price"]]
df.to_csv("data.csv", index=False)
