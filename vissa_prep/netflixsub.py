L, M, N, x = map(int,input().split())
if (L+M>=x):
    print("YES")
elif (M+N>=x):
    print("YES")
elif(N+L>=x):
    print("YES")
else:
    print("NO")
