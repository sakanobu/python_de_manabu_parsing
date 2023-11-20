# def calc(s):
#     return float(s)


# def calc(s):
#     pos = s.find("+")
#
#     if 0 < pos:
#         left = s[:pos]
#         right = s[pos + 1 :]
#
#         return float(left) + float(right)
#
#     return float(s)


def calc(s):
    return sum(map(float, s.split("+")))


if __name__ == "__main__":
    # ケース 1
    assert calc("1") == 1.0

    # ケース 2
    assert calc("1+2") == 3.0
    assert calc("10+200") == 210.0
    assert calc("1.5+3") == 4.5

    # ケース 3
    assert calc("1+2+3") == 6.0
    assert calc("1+2+3+4") == 10.0
    assert calc("1.5+3+20") == 24.5

    # ケース 4
    # assert calc("1+2*3") == 7.0
    # assert calc("1*2+3") == 5.0

    # ケース 5
    # assert calc("1-2") == -1.0
    # assert calc("1-2-3") == -4.0

    # ケース 6
    # assert calc("1+2*3") == 7.0
    # assert calc("(1+2)*3") == 9.0

    print("All Test Passed")
