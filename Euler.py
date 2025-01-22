#needs: odf odfpy pandas
#pip install odf 
#pip install odfpy 
#pip install pandas
#pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

#Matplotlib
plt.xlabel('X-Richtung')
plt.ylabel('Y-Richtung')
plt.title('Waagerechter Wurf')

#Initialize an empty DataFrame to store the data
data = pd.DataFrame(columns=['t', 'x', 'y'])

#Schieberegler
m = 2               #Masse (kg)
C = 0.45            #Spezieller Luftwiederstandkoeffizient ((0;2])
A = 0.1963           #Querschnittfläche (m²)
vel_x = 10          #X-Startgeschwindigkeit (m/sec)
vel_y = 0          #Y-Startgeschwindigkeit (m/sec)
d_t = 0.1          #Zeitschritt (sec)
t_max = 2        #Maximale Zeit (sec)

#Konstanten
g = 29.81            #Gravitation
S = 1.29            #Luftdichte

#Initialisierung
x = 0               #Strecke in x Richtung (m)
y = 0               #Strecke in y Richtung (m)
F = g*m             #Anziehung der Kraft der Erde
a_x = 0             #Beschleunigung in x Richtung (m) 
a_y = 0             #Beschleunigung in y Richtung (m)
F_Luft_x = 0 #Luftwiederstandkoeffizient in x Richtung
F_Luft_x = 0          #Luftwiederstandkoeffizient in y Richtung
k = C*A*S/2
t = 0               #Zeitzählvariablen
X_Punkte = []       #Matplotlib Liste für X-Richtung
Y_Punkte = []       #Matplotlib Liste für Y-Richtung

#Bewegung
while t <= t_max:

    #Bewegung in x-Richtung
    F_Luft_x = k * vel_x**2 #Berechnung von Luftwiederstandkoeffizient in y Richtung
    a_y = (F - F_Luft_x) / m #Berechnung von Beschleunigung in y Richtung
    vel_x = a_x * d_t + vel_x #Berechnung von Delta Geschwindigkeit in y Richtung
    x = y + vel_x * d_t #Strecke in y Richtung
    X_Punkte.append(x)

    #Bewegung in y-Richtung
    F_Luft_y = k * vel_y**2 #Berechnung von Luftwiederstandkoeffizient in y Richtung
    a_y = (F - F_Luft_y) / m #Berechnung von Beschleunigung in y Richtung
    vel_y = a_y * d_t + vel_y #Berechnung von Delta Geschwindigkeit in y Richtung
    y = y + vel_y * d_t #Strecke in y Richtung
    Y_Punkte.append(-y)
    
    #Ausgabe der geradigen Position und Zeit
    print(f"Zeit:","{:10.4f}".format(t), "  x:", "{:10.4f}".format(x), "    y:", "{:10.4f}".format(-y))

    #Add the current values of t, x, y to the DataFrame
    data = data._append({'t': t, 'x': x, 'y': -y}, ignore_index=True)
    
    #Add current values of x, y to Matplotlib
    X_Punkte.append(x)
    Y_Punkte.append(-y)
    
    #Nächste Zeititeration
    t += d_t        

#Export the DataFrame to an .ods file
data.to_excel('Waagerechter_Wurf.ods', engine='odf', index=False)

#Zeige Graph
plt.plot(X_Punkte, Y_Punkte, 'b-')
plt.show()