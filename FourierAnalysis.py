#Importamos los paquetes necesarios para resolver el problema
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile as sciwav
import numpy.fft as fft
#Leemos el archivo usando las funciones de wavfile 
dt = 1. / ( 44100 )
Tr = sciwav.read('trumpet.wav')[1]
Vi = sciwav.read('violin.wav')[1]
#Organizamos los datos en una lista para cada uno de los instrumentos 
fTr = fft.fft(Tr)
fVi = fft.fft(Vi)
#Calculamos las frecuencias asociadas y hacemos el shift de modo que deje las frecuencias zero en el centro del espectro
Vifreq = fft.fftfreq(Vi.size,d=dt)
Trfreq = fft.fftfreq(Tr.size,d=dt)
#Organizamos dos matrices que van a contener los datos para graficarlos
v = [[],[]]
t = [[],[]]
#Organizamos los datos de forma que tomemos nada mas las frecuencias positivas y los ponemos en la matriz del instrumento adecuado
for i in range(Vifreq.size):
    if(Vifreq[i]>=0):
        v[0].append(Vifreq[i])
        v[1].append(fVi[i].real)
for i in range(Trfreq.size):
    if(Trfreq[i]>=0):
        t[0].append(Trfreq[i])
        t[1].append(fTr[i].real)
#Establecemos las variables adecuadas para hacer la grafica dividida en dos subplots
f,(ax1,ax2) = plt.subplots(2, sharex=True)
#f.set_size_inches(10.,10.)
ax1.plot(v[0],v[1])
ax1.set_title("Espectros de Frecuencia")
ax2.plot(t[0],t[1])
ax2.set_xlabel("Frecuencias")
plt.savefig('ViolinTrompeta.png')
plt.close()
#Definimos la funcion que elimina la frecuencia fundamental. Toma como parametro la transformada de fourier de un conjunto de datos y un intervalo de frecuencias y retorna la lista de los datos modificados en el dominio del tiempo.
def filtrofun(fData,Fr):
	#Definimos una copia de los datos
	fData1 = np.array(fData)	
	#Tomamos la norma de esos datos
	DataNorm = abs(fData1)
	#Tomamos el maximo de los datos normados
	Mma = np.ndarray.max(DataNorm)
	#Buscamos la posicion de este maximo en los datos normados
	n_fun = np.where(DataNorm==Mma)[0][0]
	#Ponemos en cero la amplitud de la posicion que encontramos anteriormente
	fData1[n_fun]=0.0
	#Hacemos lo mismo para los datos de frecuencias negativas
	fData1[(-1)*n_fun]=0.0
	#Realizamos la transformada inversa de los datos
	ModData = fft.ifft(fData1)
	#Definimos las variables necesarias para hacer las graficas antes y despues del accionar del filtro
	f,(ax1,ax2) = plt.subplots(2, sharex=True)
#	f.set_size_inches( 10.,10. )
	ax1.plot(Fr,DataNorm)
	ax2.plot(Fr,abs(fData1))
	plt.savefig("violin_fundamental.png")
	#Retorna la parte real de la transformada inversa de los datos
	return ModData.real
#Definimos la funcion del filtro pasa altas que recibe como parametros la transformada de Fourier de unos datos y una lista de frecuencias. Retorna la lista de los datos modificados en el dominio del tiempo
def filtropasaaltas(fData,Fr):
	#Realizamos una copia de los datos
	ModData = fData.copy()
	#Hacemos cero los datos en todas las posiciones en las que la magnitud de la frecuencia sea menor a 2000
	ModData[abs(Fr) < 2000] = 0.0
	plt.plot(Fr,abs(ModData))
	plt.savefig("Violin_pasaaltas.png")
	plt.close()
	#Hacemos la transformada inversa de los datos modificados
	ModData = fft.ifft(ModData)	
	#Retorna la parte real de la transformada inversa
	return ModData.real
#Definimos la funcion filtro pasa bajas que recibe como parametros la transformada de Fourier de unos datos y una lista de frecuencias. Retorna la lista de datos modificados en el dominio del tiempo	
def filtropasabajas(fData, Fr):	
	#Hacemos una copia de los datos 
	ModData = fData.copy()
	#Hacemos cero los datos en todas las posiciones en las que la magnitud de la frcuencia sea mayor a 2000
	ModData[abs(Fr) > 2000] = 0.0

	plt.plot(Fr,abs(ModData))
	plt.savefig("Violin_pasabajas.png")
	plt.close()
	#Realizamos la transformada inversa de los datos modificados
	ModData = fft.ifft(ModData)
	#Retorna la parte real de la transformada inversa
	return ModData.real
#Definimos la funcion filtro pasabanda que recibe como parametros la transformada de Fourier de unos datos, una lista de frecuencias y la mitad del ancho de banda que se quiere filtrar. Retorna la lista de los datos modificados en el dominio del tiempo 
def filtropasabanda(fData,Fr,k):
	#Hacemos una copia de los datos
	ModData = fData.copy()
	#Obtenemos la norma de los datos
	DataNorm = abs(ModData)
	#Tomamos el maximo de los datos normados
	Mma = np.ndarray.max(DataNorm)
	#Encontramos la posicion donde esta dicho maximo
	p = np.where(DataNorm == Mma)[0][0]
	#Iniciamos una lista que contendra los valores en norma que seran los que pasan en el filtro. Iniciamos con los maximos tanto en las frecuencias positivas como en 		las negativas 
	n = [DataNorm[p],DataNorm[-p]]
	#Hacemos un ciclo que va a agregar los valores que queremos
	for i in range(k):
		#El anterior en las positivas
		n.append(DataNorm[p-(i+1)])
		#El anterior en las negativas
		n.append(DataNorm[-p+(i+1)])
		#El seguiente en las positivas
		n.append(DataNorm[p+(i+1)])
		#El siguiene en las negativas
		n.append(DataNorm[-p-(i+1)])
	#Hacemos ahora un ciclo que selecciona los valores que queremos
	for i in range(len(ModData)):
		#Verificamos si el valor en cuestion esta en la lista de las normas
		if abs(ModData[i]) in n:	
			ModData[i] = ModData[i]
		#Si no esta, lo hacemos cero
		else:	
			ModData[i] = 0.0
	#Hacemos la grafica de los que queda
	plt.plot(Fr,abs(ModData))
	plt.savefig("Violin_pasabanda.png")
	plt.close()
	#Hacemos la transformada inversa 
	ModData = fft.ifft(ModData)
	#Retornamos la parte real de la transformada inversa 
	return ModData.real

filtropasabanda(fVi,Vifreq,1000)
filtropasaaltas(fVi,Vifreq)
filtropasabajas(fVi,Vifreq)
ModViolin = filtrofun(fVi,Vifreq)
print ModViolin
sciwav.write('violin_pico.wav',44100,ModViolin)
	
