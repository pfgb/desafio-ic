t = int(input())

for i in range(t):
    string = input()
    string = string.split(" ")
    total_loops = 0
    a, b = int(string[0]), int(string[1])
    while (a != b) and (b != 0) and (a != 0):
        if a > b:
            n = a // b
            if a % b == 0:
                total_loops += n - 1
                a = b
            else:
                total_loops += n
                a -= n * b
        else:
            n = b // a
            if b % a == 0:
                total_loops += n - 1
                a = b
            else:
                total_loops += n
                b -= n * a
    print(total_loops)
