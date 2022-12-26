def myPrint(string: str):
    tab = 0
    tabStr = "    "
    for char in string:
        if char in "([{":
            # print()
            # print(tabStr * tab, end=char)
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
        ...
    ...