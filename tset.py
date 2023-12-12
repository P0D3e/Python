import time
message = input("Input an only english sentence: ")
start_time = time.time()
test = 0
while test < 1000000:
    message = message.replace('o', 'E')
    message = message.replace('i', 'E')
    message = message.replace('a', 'E')
    message = message.replace('u', 'E')
    message = message.replace('y', 'E')
    message = message.replace('O', 'E')
    message = message.replace('I', 'E')
    message = message.replace('A', 'E')
    message = message.replace('U', 'E')
    message = message.replace('Y', 'E')
    test += 1
print(time.time() - start_time)