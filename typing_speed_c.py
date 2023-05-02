from time import *
import random as r

def mistake(par,usr):
    er=0
    for i in range(len(par)):
        try:
            if par[i]!=usr[i]:
                er=er+1
        except :
            er=er+1
    return er
        
def speed_time(time_s,time_e,user):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(user)/time_R
    return round(speed)
    
test=["Manish is good boy. You can try this man for your business","Welcome to the world of youtube","Hello this is new world"]
test1=r.choice(test)
print("*****typing speed*****")
print(test1)
print()
print()
time_1=time()

testinput=input("Enter :")
time_2=time()
print('Speed :',speed_time(time_1,time_2,testinput),"w/sec")
print("Error :",mistake(test1,testinput))
