def fun(lis):
    result = []
    if lis == []:
        return 0
    if not isinstance(lis, list):
        return len([lis])
    return fun(lis[0]) + fun(lis[1:])

print(f"""
fun([["a", "b", [3, [4, 5], 6]], ["c", "d"]]) => {fun([["a", "b", [3, [4, 5], 6]], ["c", "d"]])},
fun([2, ["t", 5, "w"], [3, ["h", 4, [7, 9], "e"]], "x"]) => {fun([2, ["t", 5, "w"], [3, ["h", 4, [7, 9], "e"]], "x"])}
fun([1, 2, 3, 4, 5]) => {fun([1, 2, 3, 4, 5])}
fun([1, [2, [3, [4, 5], 6]], 7, 8, 9]) => {fun([1, [2, [3, [4, 5], 6]], 7, 8, 9])}
fun([[[[[]]]]]) => {fun([[[[[]]]]])}
""")