m = input()
n = input()

n = list(n)

char = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

even = ["0", "2", "4", "6", "8", "0", "2", "4", "6", "8"]

odd = ["1", "3", "5", "7", "9", "1", "3", "5", "7", "9"]

flag = False

if char.index(n[0]) > 4:
    flag = True

m = int(m)
for i in range(m):
    n_i = char.index(n[i])
    if (i == 0) and (n_i > 4):
        n[i] = even[n_i]
    elif i == m - 1:
        n[i] = odd[n_i]
        if n_i > 4:
            n_ant = even.index(n[i - 1])
            n[i - 1] = odd[n_ant]
    elif n_i > 4:
        n[i] = even[n_i]
        n_ant = even.index(n[i - 1])
        n[i - 1] = odd[n_ant]
    else:
        n[i] = even[n_i]

if flag:
    n = ["1"] + n

print("".join(n))
