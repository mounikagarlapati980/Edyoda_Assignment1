if __name__=='__main__':
    n=int(input())
    lst=[]
    for i in range(n):
        lst.append(int(input()))
    square=list(map(lambda x: x**2,lst))
    print(square)