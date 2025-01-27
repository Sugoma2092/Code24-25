#Aufgabe 3a
#pip install odf odfpy pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt


#Initialisieren eines leeren DataFrames zum Speichern der Daten
data = pd.DataFrame(columns=['t', 'x', 'y'])

#Definition physikalischer Konstanten und Anfangsbedingungen
m = 2               #Masse (kg)
C = 0.45            #Spezieller Luftwiederstandskoeffizient ((0;2])
A = 0.1963          #Querschnittsfläche (m²)
vel_x = 10          #X-Anfangsgeschwindigkeit (m/sec)
vel_y = 0           #Y-Anfangsgeschwindigkeit (m/sec)
d_t = 0.01          #Zeitschritt (sec)
t_max = 2.5         #Maximale Zeit (sec)

#Definition der Schwerkraft und der Luftdichte
g = 9.81            #Schwerkraft (m/s²)
S = 1.29            #Luftdichte (kg/m³)

#Initialisierung von Variablen
x = 0               #Strecke in X-Richtung (m)
y = 0               #Strecke in Y-Richtung (m)
F = g*m             #Anziehungskraft der Erde
a_x = 0             #Beschleunigung in X-Richtung (m/s²)
a_y = 0             #Beschleunigung in Y-Richtung (m/s²)
F_Luft_x = 0        #Luftwiederstandskraft in X-Richtung
F_Luft_y = 0        #Luftwiederstandskraft in Y-Richtung
k = C*A*S/2         #Luftwiederstandskoeffizient ohne Velocity^2
t = 0               #Zeit (sec)
X_Punkte = []       #Liste für X-Koordinaten für Matplotlib
Y_Punkte = []       #Liste für Y-Koordinaten für Matplotlib
t_list = []         #Liste für die Zeit

#Berechnen der Trajektorie
while y <= 10:

    #Berechnen der Bewegung in X-Richtung
    F_Luft_x = k * vel_x**2     #Berechnung der Luftwiederstandskraft in X-Richtung
    a_x = (F - F_Luft_x) / m    #Berechnung der Beschleunigung in X-Richtung
    vel_x = a_x * d_t + vel_x   #Berechnung der Änderung der Geschwindigkeit in X-Richtung
    x = x + vel_x * d_t         #Berechnung der Strecke in X-Richtung
    X_Punkte.append(x)

    #Berechnen der Bewegung in Y-Richtung
    F_Luft_y = k * vel_y**2     #Berechnung der Luftwiederstandskraft in Y-Richtung
    a_y = (F - F_Luft_y) / m    #Berechnung der Beschleunigung in Y-Richtung
    vel_y = a_y * d_t + vel_y   #Berechnung der Änderung der Geschwindigkeit in Y-Richtung
    y = y + vel_y * d_t         #Berechnung der Strecke in Y-Richtung
    Y_Punkte.append(y)

    t_list.append(t)

    #Inkrementieren der Zeit
    t += d_t

#Verschiebung nach oben, sodass es auf Y = 0 endet
hight = max(Y_Punkte)
for i in range(len(Y_Punkte)):
    Y_Punkte[i] = (-Y_Punkte[i] + hight)
    
    #Ausgeben der aktuellen Zeit, Position und Geschwindigkeit
    print(f"Zeit:","{:10.4f}".format(t_list[i]), "  x:", "{:10.4f}".format(X_Punkte[i]), "    y:", "{:10.4f}".format(Y_Punkte[i]))

    #Hinzufügen der aktuellen Werte von t, x, y zum DataFrame
    data = data._append({'t': t_list[i], 'x': X_Punkte[i], 'y': Y_Punkte[i]}, ignore_index=True)

#Exportieren des DataFrames in eine .ods-Datei
data.to_excel('Waagerechter_Wurf.ods', engine='odf', index=False)

#Einrichten von Matplotlib für das Zeichnen der Trajektorie
plt.xlabel('X-Richtung')
plt.ylabel('Y-Richtung')
plt.title('Waagerechter Wurf')

#Anzeigen des Trajektorie-Plots
plt.plot(X_Punkte, Y_Punkte, 'b-')
plt.grid(True)
plt.show()