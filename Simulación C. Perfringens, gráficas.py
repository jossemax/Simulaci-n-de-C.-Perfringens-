
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#Parámetros biológicos
r = 5.2
K_high = 1e9   #alta disponibilidad
K_med  = 1e8   #disponibilidad media
K_low  = 1e7   #baja disponibilidad

Ks = {'Alto': K_high, 'Medio': K_med, 'Bajo': K_low}

#Población inicial: 1% de K
def N0_from_K(K):
    return 0.01 * K

#Tiempo de simulación en horas 
t_max = 1.5
t_points = 2000
t = np.linspace(0, t_max, t_points)


#Ecuación logística
#dN/dt = r * N * (1 - N/K)

def logistic(N, t, r, K):
    return r * N * (1 - N / K)

#Simulación para cada K dado
def simulate_logistic(K, r, t):
    N0 = N0_from_K(K)
    sol = odeint(lambda N, tt: logistic(N, tt, r, K), N0, t)

    return sol.ravel()


#Simulaciones

results = {}
for label, Kval in Ks.items():
    N = simulate_logistic(Kval, r, t)
    results[label] = {'K': Kval, 'N': N, 'N0': N0_from_K(Kval)}


#Cálculo de tiempo para alcanzar el 90% de K

def time_to_reach_fraction(t, N, K, fraction=0.9):
    target = fraction * K
    #Si ya empieza por encima del target se devuelve un 0 
    if N[0] >= target:
        return 0.0
    
    f = interp1d(N, t, bounds_error=False, fill_value=(t[0], t[-1]))
    return float(f(target))


#Gráficas 
plt.rcParams.update({
    'figure.figsize': (8,5),
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'lines.linewidth': 2,
})

colors = {
    'Alto': 'blue',   
    'Medio': 'green', 
    'Bajo': 'red'    
}


#Gráficas individuales

for label, data in results.items():
    plt.figure()
    plt.plot(t * 60, data['N'], color=colors[label], label='Crecimiento bacteriano')

    #Línea de K (capacidad de carga)
    plt.axhline(data['K'], color=colors[label], linestyle='--', alpha=0.7,
                label=f'Capacidad de carga K = {data["K"]:.0e}')

    #Población inicial
    plt.scatter([0], [data['N0']], color='black', s=70, zorder=5,
                label=f'Población inicial N0 = {data["N0"]:.0e}')

    #90% de K
    K90 = 0.9 * data['K']
    plt.axhline(K90, color='gray', linestyle=':', linewidth=2,
                label='90% de K')
    plt.text(t[-1]*60*0.65, K90*1.02, '90% de K', fontsize=12, color='gray')

    plt.title(f'Crecimiento de C. perfringens\nEscenario de nutrientes: {label}')
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel('Población bacteriana (células/mL)')
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


# Gráfica comparativa de los 3 escenarios de nutrientes

plt.figure(figsize=(9,6))

for label, data in results.items():
    plt.plot(t*60, data['N'], label=f'{label} (K={data["K"]:.0e})',
             color=colors[label])
plt.axhline(0.9 * K_high, color='black', linestyle=':', linewidth=2,
            label='Referencia: 90% de K_alto')

plt.title('Comparación del crecimiento de C. perfringens\nBajo diferentes disponibilidades de nutrientes')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Población bacteriana (escala log)')
plt.yscale('log')
plt.grid(alpha=0.3, which='both')
plt.legend()
plt.tight_layout()
plt.show()

# Mostrar tiempo para alcanzar 90% de K

fraction = 0.90
print(f"\nTiempo para alcanzar el {fraction*100:.0f}% de K (r = {r} h^-1):")
for label, data in results.items():
    time_hr = time_to_reach_fraction(t, data['N'], data['K'], fraction=fraction)
    time_min = time_hr * 60
    print(f" - {label:5s}: K = {data['K']:.1e} -> t({int(fraction*100)}%K) ≈ {time_min:.1f} minutos ({time_hr:.3f} h)")

