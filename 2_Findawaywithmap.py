if __name__=='__main__':
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(int(input()))
    triple=list(map(lambda x : x*3,lst))
    print(triple)