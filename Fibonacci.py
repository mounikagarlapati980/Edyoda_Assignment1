first=0
second=1
third=first+second
while third<=50:
    print(third,end=" ")
    third=first+second
    first=second
    second=third
   