def ruler(n):
    for i in range(1,(n//10)+1):
        print(" "*9, end='')
        print(i, end='')
    print()
    for i in range(1,n+1):
        print(i%10, end='')