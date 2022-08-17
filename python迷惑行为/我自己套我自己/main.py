

N = 800
"""
a1 = []
a2 = []
a3 = []
...
a799 = []

"""

string = "".join(f"a{i} = []\n" for i in range(N))
for i in range(N):
    string += f"a{i}.append(a{N - 1})\n" if i == 0 else f"a{i}.append(a{i - 1})\n"

for i in range(N):
    string += f"print(a{i})\n"

exec(string)
