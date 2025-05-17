n=int(input())
result=""
for i in range(n):
    line=input("enter the passage")
for i in line:
    if i in "aeiouAEIOU":
        result+=i.upper()
    else:
        i.lower()
        result+=i.lower()
print(result)
