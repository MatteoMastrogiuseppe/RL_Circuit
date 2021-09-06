# definizione librerie
import serial
import numpy as np
from drawnow import drawnow
import matplotlib.pyplot as plt
import pickle
from scipy.optimize import curve_fit


# definizione della porta di comunicazione seriale
arduino = serial.Serial('COM3', 9600)
x = []
y = []

# inizio acquisizione
for i in range(100):
    read = arduino.readline()
    time, voltage  = [float(k) for k in read.decode('ascii').split(";")]
    x.append(time * 1e-6)
    y.append(voltage)
# fine acquisizione

# salvataggio dei dati in un file
def Store (obj, name, path): 
	f = open ( path+name, 'wb')
	pickle.dump(obj,f)
	f.close()

R = 110
time_array = np.array(x)
voltage_array = np.array(y)
current_array = voltage_array/R
charge = np.column_stack((time_array, voltage_array))
Store(charge, 'charge4_10', '')

def exponential(x,a,tau):
    return a*(1-np.exp(-1/tau*x))
# interpolazione dei dati sperimentali
popt2, _ = curve_fit(exponential,  time_array,  current_array)

print(popt2)
print("Inductance is: ",popt2[1])
print("(i_inf = ", 5/R, ")")