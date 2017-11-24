count = {}
while True:
    sent = input("Enter some sentences (enter END to terminate) ")
    if sent == "END":
        break
    list = sent.split(" ")
    for i in list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
for x in count:
    print(x, count[x])