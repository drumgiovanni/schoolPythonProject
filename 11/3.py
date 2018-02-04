def deeprev(lst):
        if lst == []:
            return []
        elif isinstance(lst, list):
            return

        else:
            return deeprev(lst[1:]) + [lst[0]]





print(f"{deeprev([0, 1, [2, 3]])}")

