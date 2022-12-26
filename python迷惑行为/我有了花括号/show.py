import ast

string = """
a = 15
if (a == 15):{
    print(a), 
    print(a)
}
else:{
    print("no"),
    
}
"""


def myPrint(string: str):
    tab = 0
    tabStr = "    "
    for char in string:
        if char in "([{":
            print(char, end="")
            tab += 1
            print("\n", end=tabStr * tab)
        elif char in ")]}":
            print()
            tab -= 1
            print(tabStr * tab, end=char)
        elif char == ",":
            print(char)
            print(tabStr * tab, end="")
        else:
            print(char, end="")


myPrint(ast.dump(ast.parse(string)))

a = 1
if (a == 1): {
    print(a)
}
