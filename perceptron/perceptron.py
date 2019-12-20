import random

def perceptron():
    weight1=round(random.uniform(-0.5,0.5),1)
    weight2=round(random.uniform(-0.5,0.5),1)
    weight0=round(random.uniform(-0.5,0.5),1)

    x0=-1
    alpha=0.09
    flag=True
    output=1
    thetha=0
    dataset=((0,0,0),(1,0,0),(0,1,0),(1,1,1))
    while(flag==True):
        print("run")
        flag=False
        for examp in dataset:
            sum=(examp[0]*weight1)+(examp[1]*weight2)
            thetha=weight0*x0
            if(sum+thetha>=0):
                output=1
            else:
                output=0
            if((output-examp[2])!=0):
                weight1=round(weight1+(alpha*(examp[2]-output)*examp[0]),1)   
                weight2=round(weight2+(alpha*(examp[2]-output)*examp[1]),1)   
                weight0=round(weight0+(alpha*(examp[2]-output)*x0),1)   
                flag=True
    print(weight1,weight2,weight0)
    return (weight1,weight2,weight0)
perceptron()

