def checklist(x):
    content = ""
    time = 0
    for i in x:
        if time == 0:
            content = i
        else:
            if not i == content:
                print(False)
                return False
            else:
                print(True)
                return True
        time += 1
checklist([1, 1, 1, 1])
checklist([1, 0, 1, 1])
checklist([-1, -1, -1])
checklist(["abc", "abc", "abc"])