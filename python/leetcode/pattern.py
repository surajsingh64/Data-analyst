row=int(input("enter the row"))
#column=int(input("enetr the column "))
"""for i in range(row):
    for j in range(column):
        print("*",end=" ")
    print()"""
"""
* * * * 
* * * *
* * * *
* * * *
* * * *
"""
"""for i in range(1,row+1):
    for j in range(1,column+1):
        if i==1 or i==row:
            print("*",end="")
        elif j==1 or j==column:
            print("*",end="")
        else:
            print(" ",end="")
    print()

****
*  *
*  *
*  *
****
"""
"""for i in range(row,0,-1):
    for j in range(i):
        print("*",end="")
    print()
*****
****
***
**
*
"""
"""
for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=row-i:
            print(" ",end="")
        else:
            print("*",end="")
    print()
    *
   **
  ***
 ****
*****
"""
"""
for i in range(1,row+1):
    for j in range(1,row+1):
        if i>=j:
            print(i,end="")
    print()
1
22
333
4444
55555
"""
"""count=1
for i in range(1,row+1):
    for j in range(1,row+1):
        if i>=j:
            
            print(count,end=" ")
            count+=1
    print()
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
"""
for i in range(1,row+1):
    for j in range(1,row+1):
        if j<=i:
            print("*",end="")
    space=2*row-2*i
    for k in range(space):
        
        print(" ",end="")
    for l in range(1,row+1):
        if l<=i:
            print("*",end="")
    print()
for i in range(row,0,-1):
    for j in range(row,0,-1):
        if j<=i:
            print("*",end="")
    space=2*row-2*i
    for k in range(space):
        
        print(" ",end="")
    for l in range(row,0,-1):
        if l<=i:
            print("*",end="")
    print()
