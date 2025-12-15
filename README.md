# Simulación de *C.Perfringens*
Reporte de simulación del crecimiento poblacional de Clostridium Perfringens

En este repositorio se adjuntan los códigos en Pyton y los resultados obtenidos de las simulaciones del crecimiento poblacional de la bacteria Clostridium Perfringens utilizando el modelo logístico determinista.

## Parámetros Generales de la simulación.

Se definieron tres escenarios de disponibilidad de nutrientes, que determinan la Capacidad de Carga (**K**):

| Escenario | Capacidad de Carga (K) | Población Inicial (N₀) |
| :---: | :---: | :---: |
| Alta | 1.0 x 10⁹ bacterias | 1% de K (1.0 x 10⁷) |
| Medio | 1.0 x 10⁸ bacterias | 1% de K (1.0 x 10⁶) |
| Baja | 1.0 x 10⁷ bacterias | 1% de K (1.0 x 10⁵) |

* **Tasa Intrínseca de Crecimiento (r):** La duplicación de la bacteria es de 8 minutos, por lo tanto, el valor que se utilizó para r fue de 5.2 h⁻¹, lo que equivale al mismo periodo de tiempo, pero ajustado el valor usando como medida la hora.

## Simulación Gráfica: Analisis deñ Tiempo Constante

La primera simulación se enfocó en graficar el crecimiento logístico y calcular el tiempo necesario para alcanzar el 90% de la Capacidad de Carga (K) en cada uno de los tres escenarios.

<img width="1834" height="918" alt="Captura%20de%20pantalla%202025-11-20 220158" src="https://github.com/user-attachments/assets/bf04758c-99cf-4f69-aaf2-5c9fa3e4b036" />

En esta imagen se puede corroborar lo mencionado con anterioridad, las tres gráficas coinciden con su crecimiento exponencial, y el tiempo en alcanzar su respectivo 90% de población fue el mismo, la diferencia es la población que cada escenario alcanzó.
La población final del escenario con una Capacidad de Carga alta es 100 veces mayor la población, si lo comparamos con el escenario con Capacidad de Carga baja.

## Simulación con discos de Petri

Esta simulación tuvo un enfoque más realista, simulando el crecimiento poblacional bacteriano en los discos de Petri, que son comúnmente utilizados para realizar cultivos físicos en los laboratorios.
En este caso se usaron puntos para simular  cúmulos de bacterias, 1 punto = 100,000 bacterias.
Por lo tanto en nuestros tres escenarios se observaron las siguientes diferencias:
* El escenario bajo en el inicio se observa 1 punto, que es el 1% de 1e7.
* Al terminar la simulación, el escenario bajo tan solo prsenta 100 puntos, mientras que el escenario medio cuenta con 1,000 puntos y el escenario alto se satura con 10,000 puntos, que realizando la respectiva multiplicación por 100,000 coincide con la Capacidad de Carga deseada.

<img width="1258" height="470" alt="Captura de pantalla 2025-12-14 181315" src="https://github.com/user-attachments/assets/a9ceadaf-4621-4586-83f9-cebc0e43f5cf" />

Aquí se observa el inicio de la simulación en su valor más bajo, representando el 1% de cada población.

<img width="1253" height="454" alt="Captura de pantalla 2025-12-14 181420" src="https://github.com/user-attachments/assets/222e29f9-292a-4ac9-b48d-ad0d05bf0d8c" />

Al término de la simulación la diferencia en su población final es evidente. 

## Conclusiones
El realizar estas simulaciones, nos permitió demostrar de una manera analítica y visual los principios fundamentaes de nuestro Modelo Logístico Determinista en su aplicación al crecimiento de *C. Perfringens*. 
* El tiempo de crecimiento es independiente al valor absoluto de K, el valor del tiempo está determinado unicamente por la tasa intrínseca de crecimiento, y por la población inicial. Lo que se pudo corroborar al obtener un crecimiento al 90% en un tiempo de 78 minutos aproximadamente en cada escenario.
* La densidad absoluta está limitada por K, puesto que en la simulación con los discos de Petri se demostró que, aunque los tres escenarios alcanzan la saturación al mismo tiempo, la magnitud absoluta de la población (Capacidad de Carga) está directamente controlada por K.
