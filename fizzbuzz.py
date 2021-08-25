i=0
a=""
b=""
while i <= 100:
    if i % 2 == 0:
        print(str(i) + "Fizz" + a + b)
        if i % 3 == 0:
            a = "Buzz"
            if i % 5 == 0:
                b = "Pop!"
            else:
                b = ""
        else:
            a = ""
    else:
        print(str(i) + "...")
    i+=1