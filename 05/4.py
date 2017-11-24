import random
rnd = int(random.randrange(10))
def abs_val(x):
    if x >= 0:
        return print(x)
    elif x < 0:
        return print(x * -1)

for i in range(rnd):
    x = random.randrange(-10, 10)
    print(f"x={x}", end = " => ")
    abs_val(x)