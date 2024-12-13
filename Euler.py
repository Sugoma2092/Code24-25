#Schieberegler
m = 68.1
C = 0.5
A = 5
vel_x = 0.1
vel_y = 0.1
d_t = 0.5
t_max = 100

# Konstanten
g = 9.81
S=1.29 #Luftdichte

#Initialisierung
x = 0
y = 0
t = 0
F = g*m 
a_x = 0
a_y = 0
Besch_x = 0
Besch_y = 0
d_v_x = 0
d_v_y = 0
v_x = 0
v_y = 0
d_S_x = 0
d_S_y = 0

#Bewegung
while t < t_max:
    t += d_t
    
    F_Luft = 0.5*S*A*C #ohne die Geschwindigkeit
    
    # Bewegung in x-Richtung
    Besch_x += F-(vel_x*F_Luft)
    a_x = Besch_x / m
    d_v_x= a_x * d_t
    v_x +=d_v_x
    d_S_x = v_x * d_t
    x+=d_S_x
    
    # Bewegung in y-Richtung
    Besch_y += F-(vel_y*F_Luft)
    a_y = Besch_y / m
    d_v_y= a_y * d_t
    v_y +=d_v_y
    d_S_y = v_y * d_t
    y+=d_S_y
    
    # Ausgabe
    print(f"Zeit:", t, "x:", x, "y:", y)