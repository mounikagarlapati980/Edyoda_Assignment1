even=0
odd=0
number=int(input())
for i in range(number):
    key=int(input())
    if key%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)