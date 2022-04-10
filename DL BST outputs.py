import random
import string


def Upper_Lower_string(length):
    result = ''.join(
        (random.choice(string.ascii_lowercase) for x in range(length)))
    return result

N = 1000

howManyFiles_NInterval = 10


for times in range(howManyFiles_NInterval):
    filename = "outputs/outputTest_%s.txt" % (times+1)
    f = open(filename, 'a')
    tempList = random.sample(range(1000000, 9999999), ((times+1)*N))
    print(len(tempList))
    for x in range((times+1)*N):
        f.write(Upper_Lower_string(12) + " " + Upper_Lower_string(12) + " " + str(tempList[x]) + "\n")
    f.close()
