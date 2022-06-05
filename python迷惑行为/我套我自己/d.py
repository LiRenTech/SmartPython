dic = {}
dic["d"] = dic

print(dic)

print(eval("{'d': {...}}"))
d1 = {}
d2 = {}

d1["1"] = d2
d2["2"] = d1

print(d1, d2)
