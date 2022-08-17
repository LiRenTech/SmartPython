# a1 = ["a1"]
# a2 = ["a2"]
# a3 = ["a3"]
# a1.append(a3)
# a2.append(a1)
# a3.append(a2)
# print(a1)
# print(a2)
# print(a3)

N = 800
string = "".join(f"a{i} = []\n" for i in range(N))
for i in range(N):
    string += f"a{i}.append(a{N - 1})\n" if i == 0 else f"a{i}.append(a{i - 1})\n"

for i in range(N):
    string += f"print(a{i})\n"

exec(string)
