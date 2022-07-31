def upperlower(string):
    up=0
    low=0
    for i in string:
        x=ord(i)
        if x>=65 and x<=90:
            up+=1
        elif x>=97 and x<=122:
            low+=1
    return up,low
if __name__=="__main__":
    string=input()
    up,low=upperlower(string)
    print("No. of Upper case characters :",up)
    print("No. of Lower case Characters :",low)
