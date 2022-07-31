def sumlst(lst):
    su=0
    for i in lst:
        su+=i
    return su
if __name__=="__main__":
    n=int(input())
    lst=[]
    for i in range(n):
        val=int(input())
        lst.append(val)
    res=sumlst(lst)
    print(res)