import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

#Tasa de crecimiento
r = 5.2  
#Disponibilidad de nutrientes
K_high = 1e9  
K_med  = 1e8  
K_low  = 1e7  

# Tiempo por hora
t_max = 1.5     
frames = 200    
dt = t_max / frames
times = np.linspace(0, t_max, frames)

#Se eligen 10,000 puntos para la representación de las bacterias (1 punto equivale a cienmil bacterias)
MAX_DOTS = 10000

def logistic_analytical(t, K, r, N0):
   #Solución de la ecuación logística 
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

# Generación de los puntos aleatorios dentro de cada círculo
def generate_bacteria_positions(num_points, radius=1.0):
    if num_points <= 0:
        return np.empty((0, 2))
    theta = np.random.uniform(0, 2*np.pi, num_points)
    # La raíz cuadrada de r para una dispersion uniforme
    r_pos = radius * np.sqrt(np.random.uniform(0, 1, num_points))
    
    x = r_pos * np.cos(theta)
    y = r_pos * np.sin(theta)
    return np.column_stack((x, y))

#Generación de las figuras 

fig, axes = plt.subplots(1, 3, figsize=(15, 6))
fig.suptitle(f'Visualización de Densidad Bacteriana (t = 0.00 h)', fontsize=16)

scenarios = [
    {'name': 'Baja Disponibilidad', 'K': K_low,  'ax': axes[0], 'color': 'tab:blue'},
    {'name': 'Media Disponibilidad', 'K': K_med,  'ax': axes[1], 'color': 'tab:orange'},
    {'name': 'Alta Disponibilidad',  'K': K_high, 'ax': axes[2], 'color': 'tab:green'}
]

# Se inician los gráficos
scatters = []
texts = []

for s in scenarios:
    ax = s['ax']
    K_val = s['K']
    
    # Limite de los circulos
    circle = patches.Circle((0, 0), radius=1, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    
    # Ejes de los circulos
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.axis('off') 
    ax.set_title(f"{s['name']}\nK = {K_val:.0e}")
    
    # Se crea el scatter para el inicio de la simulación
    scat = ax.scatter([], [], s=10, c=s['color'], alpha=0.6)
    scatters.append(scat)
    
    # Se muestra el porcentaje de saturación
    txt = ax.text(0, -1.2, '', ha='center', fontsize=10)
    texts.append(txt)

# Animación 
def update(frame):
    current_time = times[frame]
    fig.suptitle(f'Crecimiento Bacteriano en Tiempo Real: {current_time:.2f} horas', fontsize=16)
    
    for i, s in enumerate(scenarios):
        K = s['K']
        # Usamos el 1% de K como inicio
        N0 = 0.01 * K 
        
        
        N_t = logistic_analytical(current_time, K, r, N0)
        num_visual_dots = int((N_t / K_high) * MAX_DOTS)
        offsets = generate_bacteria_positions(num_visual_dots)
        scatters[i].set_offsets(offsets)
        saturation = (N_t / K) * 100
        texts[i].set_text(f"Población: {N_t:.2e}\n({saturation:.1f}% de su K)")

    return scatters + texts

# Se realiza la animación 
anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=False)

plt.tight_layout()
plt.show()