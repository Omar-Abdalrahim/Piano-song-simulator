import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
𝑡 = np.linspace(0 ,3,12*1024)                                   #Time for the whole song (Time axis))
F=np.array([0,0,0,0,0,0,0,246.93])                              #Frequency of the first hand (third octave)
f=np.array([261.63,329.63,440,261.63,329.63,440,261.63,0])      #frequency of the second hand (fourth octave)
ti=np.array([0,0.4,0.65,1.2,1.5,1.9,2.3,2.7])                   #Time for the start of every note
Ti=np.array([0.3,0.2,0.4,0.25,0.3,0.3,0.3,0.3])                 # Time for playing the note
#amp=np.array([1,3,2,3,2,1,2,1])
N=8                                                             #Number of Notes played
x=0
i=0
while(i<N):
    #temp=np.reshape((np.sin(2*np.pi*(F[i])*t)+np.sin(2*np.pi*(f[i])*t))*[(t>=ti[i]) & (t<=ti[i]+Ti[i])],np.shape(t))
    temp =np.where((t>=ti[i])&(t<=ti[i]+Ti[i]),np.sin(2*np.pi*(F[i])*t)+np.sin(2*np.pi*(f[i])*t),0)  #Single Note
    x=x+temp
    i=i+1
    plt.plot(t,temp)

sd.play(x,3*1024)   

