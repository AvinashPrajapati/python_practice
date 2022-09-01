import pandas as pd

INF = float('inf')
graphInput = [['A', 'B', 10],
              ['B', 'D', 2],
              ['A', 'E', 10],
              ['A', 'C', 3],
              ['C', 'E', 12],
              ['E', 'D', 1],
              ]

dictGraph = {}
for i in graphInput:
    dictGraph[(i[0], i[1])] = i[2]
srcSet = set(x[0] for x in dictGraph.keys())
desSet = set(x[1] for x in dictGraph.keys())
places = srcSet.union(desSet)
rows = [x for x in places]
columns = [x for x in places]
wells = pd.DataFrame(columns=columns, index=rows)
for i in rows:
    for j in columns:
        if i != j and (i, j) in dictGraph.keys():
            wells.loc[i, j] = int(dictGraph[(i, j)])
        elif i == j:
            wells.loc[i, j] = 0
        else:
            wells.loc[i, j] = float("inf")

# Graph Operations

for k in places:
    for i in places:
        for j in places:
            if wells.loc[i, k] + wells.loc[k, j] < wells.loc[i, j]:
                wells.loc[i, j] = wells.loc[i, k] + wells.loc[k, j]
print(wells)
