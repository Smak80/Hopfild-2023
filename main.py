from DataLoader import DataLoader
from HopfildNN import HopfildNN as hopnn

d = DataLoader("data.xlsx")
data = d.get_data()
h = hopnn()
h.learn(data)
td = DataLoader("test.xlsx")
test = td.get_data()
res = h.recognize(test)
print(res)