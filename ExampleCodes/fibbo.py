
def fibbo(num):
    a , b = 0 , 1
    for i in xrange(num):
         yield a
         a , b = b , a + b

num = input("Enter a number :")
for i in fibbo(num):
    print i,


