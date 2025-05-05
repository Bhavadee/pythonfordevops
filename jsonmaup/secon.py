import json

# Step 1: Load JSON from the source file
with open('data.json', 'r') as infile:
    data = json.load(infile)

# Step 2: Modify the data (optional)
data["country"] = "India"

# Step 3: Dump JSON to a new file
with open('output.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Data has been loaded from 'data.json' and saved to 'output.json'")
