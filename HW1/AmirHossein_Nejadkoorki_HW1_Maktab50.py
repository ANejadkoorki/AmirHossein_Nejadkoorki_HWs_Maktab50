#this the first class work
n = int(input("enter the number of sentences :   "))
x = float(input("please enter the value of x : "))
jomleha = list(range(1,n + 1))
def jomlesaz(a):
    if a == 0 :
        return True
    makhraj = 0
    for i in range(1,a + 1):
        makhraj += (i * x ** i)
        jomle_aVOM = 1 / makhraj
        jomleha[a - 1] = jomle_aVOM
    jomlesaz(a - 1)
jomlesaz(n)

def sum_of_sentences(a = []):
    jam = 0
    for b in range(0,n):
        if b % 2 == 0 :
            jam += a[b]
        elif b % 2 != 0:
            jam -= a[b]
    print("the total of first",n,"sentences is : ",jam)

sum_of_sentences(jomleha)




    




















