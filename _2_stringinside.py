def reverse(string):
    str1=''
    for i in string[::-1]:
        str1+=i
    return str1
if __name__=="__main__":
    string=input()
    res=reverse(string)
    print(res)