def orgate(a,b,target):
    if(a*0.6 + b*0.6)< threshold:
        output = 0
    else:
        output = 1

    if(output != target):
        w1 = w1+a*learningRate*(target - output)
        w2 = w2+a*learningRate*(target - output)

threshold = int(input('enter the threshold value:'))
learningRate = 0.5
y = a or b
w1 = 0.6
w2 = 0.6
