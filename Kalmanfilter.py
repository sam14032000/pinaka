import numpy as np 
import math 
import scipy.integrate as integrate
from scipy.misc import derivative
#take these as raw_input from GPS module.Initiating it to zero.How does gps input it as a tuple?(Then accordingly we have to modify it)
Vb=0#airspeed Bias
Wn=0#Northern wind component 
We=0#Eastern wind component
Vg=0#Ground Velocity
gta=0#ground track angle 
Vtsensor=0#airspeed reading from sensor
AIRSerr=0#error in air speed measurment from sensor and kalman filter estimate AIRSerr=epsilon in documentation

Xwind=np.matrix([[Vb],[Wn][We]])#init filter states airspeed bias,northern and eastern wind components
Pwind=np.matrix([[0.5,0,0],[0,0.5,0],[0,0,0.5]])
Qwind=np.matrix([[0.0001,0,0],[0,0.001,0],[0,0,0.001]])
Rwind=0.5
n=0
rinput=0
#loop starts here(it is not clear on how to start the loop)
while rinput!=1:
    
    print("Reached here")


    Pwind=Pwind+Qwind#integrate here the following term but it is quite unclear on how to integrate it 

    Vn=Vg*np.cos(gta)#ground track angle
    Ve=Vg*np.sin(gta)

    Nerr=Vn-Wn#error in north component
    Eerr=Ve-We#error in east component
    Va=abs(math.sqrt(Nerr*Nerr+Eerr*Eerr))#airspeed magnitude component 
    V_tsensor=Va-Vb#true airspeed estimate
    AIRSerr=Vtsensor-V_tsensor

    #performing the kalman filter 

    if(Va>0):
        n=n+1
        C=np.array([-1,-Nerr/Va,-Eerr/Va])
        CT=np.transpose(C)
        P1=np.linalg.inv(C.dot(Pwind).dot(CT).dot(Rwind))
        K=Pwind.dot(CT).dot(P1)
        print("Over here")


        #Performing the covarience and state updates
        Xwind=Xwind+K.dot(AiRSerr)
        Pwind=Pwind_K.dot(C).dot(Pwind)
        print("Reached here")

        #outputs of the wind estimator
        Wn=Xwind[1]
        We=Xwind[2]
        Vw=abs(math.sqrt(Wn*Wn+We*We))
        Xw=math.atan2(-We,-Wn)#Xw represents the wind direction
        Whw=-Wn*math.cos(Xw)-We*math.cos(Xw)#Whw represents instantaneous head wind
        Vb=Xwind[0]
        Vt=Vb+V_tsensor#this is a much more cleaner version of true airspeed being used and will last the rest of the program for the iteration
    if(n==1):
        rinput=1



