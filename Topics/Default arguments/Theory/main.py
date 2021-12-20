# A, B, C, X, Y
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
if a <= x and b <= y:
    print("The box can be carried")
elif b <= x and c <= y:
    print("The box can be carried")
elif c <= x and  b <= y:
    print("The box can be carried")
else:
    print("The box cannot be carried")
