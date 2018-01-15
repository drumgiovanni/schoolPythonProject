def deeprev(lst):
        if not isinstance(lst, list):
            if lst == []:
                return []
            else:
                return deeprev(lst[1:]) + [lst[0]]
        else:
            for o in lst:
                if o == []:
                    return []
                else:
                    return deeprev(o[1:]) + [o[0]]

print(f"{deeprev([0, 1, [2, 3]])}")

