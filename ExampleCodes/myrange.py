def myrange(start, stop, step):
    while (start < stop):
        yield start
        start += step

for i in myrange(10, 20, 2):
    print i,
