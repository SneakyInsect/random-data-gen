import random
import string


def Upper_Lower_string(length):
    result = ''.join(
        (random.choice(string.ascii_lowercase) for x in range(length)))
    return result

N = 1000

howManyFiles_NInterval = 10

for times in range(howManyFiles_NInterval):
    filename = "output/output_%s.txt" % (times+1)
    f = open(filename, 'a')
    for x in range((times+1)*N):
        no = 1000000+x
        f.write(Upper_Lower_string(12) + " " + Upper_Lower_string(12) + " " + str(no) + "\n")
        no += 1
    f.close()