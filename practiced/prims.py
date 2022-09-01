import pandas as pd
from collections import OrderedDict

INF = float('inf')
graphInput = [['A', 'B', 4],
              ['B', 'C', 4],
              ['C', 'D', 5],
              ['C', 'E', 2],
              ['D', 'E', 3],
              ['E', 'B', 3],
              ['E', 'F', 1],
              ['F', 'B', 6],
              ['F', 'A', 6],
              ]

dictGraph = OrderedDict()
for i in graphInput:
    dictGraph[(i[0], i[1])] = i[2]
# print(dictGraph.keys())
places = []
for i in dictGraph.keys():
    if i[0] not in places:
        places.append(i[0])
for i in dictGraph.keys():
    if i[1] not in places:
        places.append(i[1])
# print(places)
V = len(places)

rows = [x for x in places]
columns = [x for x in places]
wells = pd.DataFrame(columns=columns, index=rows)
for i in rows:
    for j in columns:
        if i != j and (i, j) in dictGraph.keys():
            wells.loc[i, j] = int(dictGraph[(i, j)])
            wells.loc[j, i] = int(dictGraph[(i, j)])
        elif i == j:
            wells.loc[i, j] = 0
        # else:
        #     wells.loc[i, j] = "_"
print(wells)
# print(wells.loc['A', 'B'], wells.loc['B', 'A'])
#
parent = [None for _ in places]
parent[0] = -1

placeDis = [{i: float("INF")} for i in places]
placeDis[0][places[0]] = 0

mstSet = [{i: False} for i in places]
# mstSet[0][places[0]] = True


def selectMinimum(distances, mst):
    place = None
    min = float('inf')
    global places
    count = 0
    for i in places:
        if mst[count][i] == False and distances[count][i] < min:
            place = i
            min = distances[count][i]
        count += 1
    return place
def plac(mst, key):
    for i in mst:
        try:
            return i[key]
        except Exception as e:
            pass
def setmst(mst, key):
    for i in mst:
        try:
            if i[key] == False:
                i[key] = True
                # print(i, key)
                return
        except Exception as e:
            pass
def setplace(dis, key, value):
    for i in dis:
        try:
            if i[key]:
                i[key] = value
                return
        except Exception as e:
            pass

# print(placeDis, mstSet)/
c = 0
for _ in places:
    # MOVE TO VERTEX
    # print(placeDis, mstSet)
    u = selectMinimum(placeDis, mstSet)
    # print(u)
    setmst(mstSet, u)
    # RELAX EDGES
    c2 = 0
    for j in places:
        # print(c2, u, j)
        if (wells[u][j] != 0 and plac(mstSet, j) == False) and wells[u][j] < plac(placeDis, j):
            # print(wells[u][j])
            setplace(placeDis, j, wells[u][j])
            parent[c2] = u
        c2 += 1
    c += 1

c3 = 0
# print(places)
# print(parent)
mst = []
for i in places:
    try:
        place = parent[c3]
        # print("p1 -> p2 :", place, " -> ", i, " distance:", wells.loc[place, i])
        mst.append({(place,i): wells.loc[place, i]})
    except Exception as e:
        pass
    c3 += 1

print(mst)
