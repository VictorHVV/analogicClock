# 🕒 Reloj Analógico Dinámico con Pygame

Un elegante reloj analógico programado en Python utilizando la librería Pygame. El proyecto renderiza un reloj completamente funcional en tiempo real, incluyendo marcadores visuales para las horas y minutos, manecillas fluidas y recuadros de información de calendario (Día, Mes, Año, Día de la semana y Número de semana del año).

---

## ✨ Características

*   **Sincronización en tiempo real:** Utiliza el módulo `datetime` del sistema para una precisión absoluta.
*   **Diseño limpio y colorido:** Interfaz oscura con recuadros de colores estéticos para la información del calendario.
*   **Cálculo Trigonométrico Preciso:** Movimiento fluido de las manecillas mediante conversión de coordenadas polares a cartesianas.
*   **Marcadores dinámicos:** Rayas de minutos delgadas y rayas de horas gruesas dibujadas matemáticamente alrededor de la circunferencia.
*   **Información extendida:** Muestra el año, número de semana, día del mes, mes (abreviado) y día de la semana actual.

---

## 🛠️ Requisitos del Sistema e Instalación

Este proyecto está optimizado y probado para entornos modernos de desarrollo, incluyendo **Python 3.14+**.

### ⚠️ Nota importante sobre la instalación
Si estás utilizando versiones de Python muy recientes (como Python 3.14), la instalación estándar de Pygame clásica (`pip install pygame`) podría fallar por falta de compiladores de C++ preinstalados en tu sistema de Windows. 

Para solucionar esto de raíz, el proyecto utiliza **Pygame Community Edition (pygame-ce)**, el cual ofrece soporte directo e inmediato para intérpretes de Python modernos.

### Pasos para instalar:

1. **Clona este repositorio o descarga el archivo del código:**
   ```bash
   git clone https://github.com
   cd TU_REPOSITORIO
   ```

2. **Instala la librería compatible (Pygame Community Edition):**
   ```bash
   pip install pygame-ce
   ```
   *(Nota: Aunque se descarga como `pygame-ce`, en el código se sigue llamando e importando de forma transparente como `import pygame`).*

---

## 🚀 Cómo Ejecutar el Proyecto

Una vez que tengas la librería instalada, simplemente ejecuta el archivo principal desde tu terminal o editor de código:

```bash
python reloj_Analogico.py
```

---

## 🧠 Detalles Técnicos e Implementación

### Conversión de Coordenadas (Polares a Cartesianas)
Para posicionar los números de las horas y dibujar las manecillas en ángulos circulares, el script convierte el radio (r) y el ángulo en grados (θ) a coordenadas planas (X, Y) legibles por la pantalla de Pygame usando trigonometría básica:

```python
def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180) 
    y = r * cos(pi * theta / 180) 
    return x + width // 2, height // 2 - y
```

### Lógica de Ángulos de las Manecillas
*   **Segunderos:** Avanzan $6^{\circ}$ por cada segundo transcurrido ($360^{\circ} / 60$).
*   **Minuteros:** Calculan su ángulo sumando una fracción dependiente de los segundos actuales para lograr un movimiento progresivo.
*   **Horas:** Calculan su posición sumando la fracción de los minutos actuales, logrando que la manecilla de la hora avance de forma natural entre número y número a medida que pasa el tiempo.

---

## 👤 Autor

*   **GitHub.com/VictorHVV** - *Desarrollo del proyecto*
