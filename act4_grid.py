while True:
    n = int(input("Size: "))
    if 1 <= n <= 10:
        break
    print("Please enter a valid size between 1 and 10.")

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4}", end="")
    print()
