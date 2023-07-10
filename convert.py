import json
newdata = []

with open("wizardlm_orca.json","r") as f:
    data = json.load(f)

for d in data:
    newdata.append({"instruction":d["system"],"input":d["instruction"],"output":d["output"]})

with open("wr.json","w") as ff:
    json.dump(newdata,ff,indent=4)