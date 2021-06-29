def fattoriale(n):
    if n == 0:
        return 1
    else:
        return fattoriale (n-1) * n

print(fattoriale(5))