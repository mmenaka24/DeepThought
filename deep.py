def main():
    str = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    str = standardiseStr(str)
    if str == "42" or str == "forty two":
        print("Yes")
    else:
        print("No")


def standardiseStr(str):
    return str.lower().replace("-", " ").strip()


main()
