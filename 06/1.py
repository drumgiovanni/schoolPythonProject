total = 0
for i in range(1,1001):
    if i % 3 == 2 and i % 4 == 1:
        total += i
print(f"合計は{total:d}です。")