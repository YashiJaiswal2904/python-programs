import pandas as pd
with open("iris.data") as f:
    data = f.read()
    data = data.split("\n")
newData = []
for line in data:
    newData.append(line.split(","))
df = pd.DataFrame(newData, columns=["C1", "C2", "C3", "C4", "Type"])
df.to_excel("Py.xlsx", index=False)