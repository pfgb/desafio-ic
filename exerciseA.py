    t = int(input())
     
    for i in range(t):
        flag = True
        string = input()
        string = string.split(" ")
        n, m = int(string[0]), int(string[1])
        X_1 = [None] * n
        X_1_counts = dict()
        X_2 = [None] * n
        X_2_counts = dict()
        for j in range(n):
            X_1[j] = input().split(" ")
            for k in range(m):
                if X_1[j][k] in X_1_counts.keys():
                    X_1_counts[X_1[j][k]] += 1
                else:
                    X_1_counts[X_1[j][k]] = 1
        for j in range(n):
            X_2[j] = input().split(" ")
            for k in range(m):
                if X_2[j][k] in X_1_counts.keys():
                    if X_2[j][k] in X_2_counts.keys():
                        X_2_counts[X_2[j][k]] += 1
                    else:
                        X_2_counts[X_2[j][k]] = 1
                else:
                    print("NO")
                    flag = False
     
        keys1 = list(X_1_counts.keys())
        keys2 = list(X_2_counts.keys())
        size1 = len(keys1)
        size2 = len(keys2)
        if flag:
            if size1 != size2:
                print("NO")
                flag = False
            else:
                for j in range(size1):
                    if X_1_counts[keys1[j]] != X_2_counts[keys1[j]]:
                        print("NO")
                        flag = False
                        break
     
        if flag:
            print("YES")
