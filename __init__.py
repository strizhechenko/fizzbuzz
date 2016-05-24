output = range(1, 101)
for div, word in ((3, "fizz"), (5, "buzz"), (15, "fizzbuzz")):
    for index in xrange(div, 101, div):
        output[index - 1] = word
for n in output:
    print n
