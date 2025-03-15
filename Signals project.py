import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import math
𝑡 = np.linspace(0 ,3,12*1024)
F=np.array([0,0,0,0,0,0,0,246.93,0,0])
f=np.array([261.63,329.63,440,261.63,329.63,440,261.63,0,329.63,440])
ti=np.array([0,0.3,0.6,1,1.3,1.6,2,2.4,2.7,2.9])
Ti=np.array([0.2,0.2,0.3,0.2,0.2,0.3,0.3,0.2,0.15,0.1])
x=0
i=0
while(i<10):
    temp = (np.where((t>=ti[i])&(t<=ti[i]+Ti[i]),np.sin(2*np.pi*(F[i])*t)+np.sin(2*np.pi*(f[i])*t),0))
    x=x+temp
    i=i+1
    plt.plot(t,temp)                                      #Time Domain   (x)
#sd.play(x,3*1024) 
#plt.subplot(3,2,1) 
N=3*1024
f=np.linspace(0, 512,int(N/2))
x_f=fft(x)
x_f=(2/N)*np.abs(x_f[0:np.int(N/2)])
plt.figure()
#plt.subplot(3,2,2)
plt.plot(f,x_f)                                          #Frequency Domain (x_f)

##### Adding noise to the song #####

f1=np.random.randint(0,512,1)
f2=np.random.randint(0,512,1)
n =np.sin(2*np.pi*t*f1)+np.sin(2*np.pi*t*f2)
Xn=x+n
plt.figure()
#plt.subplot(3,2,3)
plt.plot(t, Xn)                                         #Time Domain  (Xn)

Xn_f=fft(Xn)
Xn_f=(2/N)*np.abs(Xn_f[0:np.int(N/2)])
plt.figure()
#plt.subplot(3,2,4)
plt.plot(f,Xn_f)                                      #Frequency Domain (Xn_f)

##### Finding the noise frequncies and removing them #####

i=0
j=0
noise=[]
while (True):
    if (Xn_f[i]>math.ceil(max(x_f))):
        noise.insert(j,math.floor(f[i]))
        j+=1
    if(len(noise)==2):
        break
    i+=1
𝑥filtered=Xn-(np.sin(2*np.pi*t*noise[0])+np.sin(2*np.pi*t*noise[1]))
plt.figure()
#plt.subplot(3,2,5)
plt.plot(t,𝑥filtered)                                    #Time Domain (𝑥filtered)
sd.play(𝑥filtered,3*1024)

𝑥filtered_f=fft(𝑥filtered)
𝑥filtered_f=(2/N)*np.abs(𝑥filtered_f[0:np.int(N/2)])
plt.figure()
#plt.subplot(3,2,6)
plt.plot(f,𝑥filtered_f)                                 #Frequency Domain (𝑥filtered_f)

