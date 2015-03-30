print 'Sleeping Beauty Test Script' 
import random
credence = 1
while(credence < 100):
    length = 10000
    guess = 0
    success = 0.0
    times = 0.0
    for i in range(0,length):
        state = random.randint(0,1)
        if state == 1:
            if guess % int(credence) == 0:
                success +=1
            times += 1
            guess += 1
        else:
            if guess % int(credence) != 0:
                success +=1
            times += 1
            guess += 1
            if guess % int(credence) != 0:
                success +=1
            times += 1
            guess += 1
    print "Credence: 1/" + str(credence) + "\t Success: " + str(100*success/times) + "%"
    credence += 1
