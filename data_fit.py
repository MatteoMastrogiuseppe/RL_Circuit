import serial
import numpy as np
from drawnow import drawnow
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pickle

def Store (obj, name, path):

	f = open ( path+name, 'wb')
	pickle.dump(obj,f)
	f.close()

def Retrieve (name, path):

	f = open( name, 'rb')
	obj = pickle.load(f)
	f.close()

def exponential(x,a,tau):
    return a*(1-np.exp(-1/tau*x))

R = [45.08, 49.5495, 70.8154, 110]
tau = []

for i in range(1,5):
	for j in range(1,11):
		f = open('charge'+str(i)+'_'+str(j), 'rb')
		charge = np.array(pickle.load(f))
		f.close()
		time = charge[:,0] 
		voltage = charge[:,1]
		current = voltage / R[i-1]
		popt, _ = curve_fit(exponential,  time,  current)
		tau.append(popt[1]*R[i-1])
	
	print(tau)
	tau_array = np.array(tau)
	Analysis = [np.mean(tau_array),np.std(tau_array)]
	print(Analysis)
	Store(Analysis, 'Analysis_'+str(i), '')
	tau.clear()




'''
plt.figure(figsize=(10,8))
plt.plot(time, current, 'ko', markersize=8, markerfacecolor='none', markeredgewidth=2, label = "Data")
plt.plot(time,popt[0]*(1-np.exp(-1/popt[1]*time)), 'b-', linewidth = 2, label = "Fit")
plt.xlabel("time (s)", fontsize=18)
plt.ylabel("current (A)", fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(loc = 'center right')
plt.tight_layout()
plt.savefig('plot.pdf')
plt.show()

print("Inductance is: ",popt[1])
print("(i_inf = ", 5/R, ")")
'''