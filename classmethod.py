class Power:
    def calculatepower(self,x,n):
        return x**n

if __name__=="__main__":
    x=int(input())
    n=int(input())
    pow=Power()
    print(pow.calculatepower(x,n))