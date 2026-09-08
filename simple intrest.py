def fun(p, t, r):
    return (p * t * r) / 100


p = int(input("Enter principal: "))
t = int(input("Enter time: "))
r = int(input("Enter rate: "))

res = fun(p, t, r)
print(res)
