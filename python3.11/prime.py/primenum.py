#prime number
num=int(input())
def is_prime(num):
    prime=True
    if num<2:
        prime=False
    else:
        for i in range(2,int(num**0.5),+1):
            if num%i==0:
                prime=False
                break
            if prime:
                print(num,"is a prime number.")
            else:
                print(num,"is not a prime number.")
is_prime(num)  

#Even prime number.
num=int(input())
if num==2:
    print(num,"is a even prime.")
else:
    print(num,"is not a even prime.")    