# 🕒 Dynamic Analog Clock with Pygame

A sleek analog clock programmed in Python using the Pygame library. This project renders a fully functional real-time clock, featuring smooth visual markers for hours and minutes, progressive hand movements, and stylized calendar information boxes (Day, Month, Year, Day of the week, and Week number of the year).

---

## ✨ Features

- **Real-Time Synchronization:** Uses the system's `datetime` module for absolute time accuracy.
- **Clean & Colorful Design:** Dark interface contrast with color-coded boxes for clear calendar visualization.
- **Precise Trigonometric Calculation:** Smooth hand rotation using polar-to-cartesian coordinate conversions.
- **Dynamic Dial Markers:** Mathematically renders thin ticks for minutes and thick ticks for hours around the rim.
- **Extended Info Display:** Tracks current year, ISO week number, day of the month, abbreviated month, and abbreviated day of the week.

---

## 🛠️ System Requirements & Installation

This project is optimized and tested for modern development environments, including **Python 3.14+**.

### ⚠️ Important Note on Installation

If you are using highly recent versions of Python (such as Python 3.14), the classic Pygame installation (`pip install pygame`) might fail due to the lack of pre-built C++ wheels for your OS.

To solve this natively, this project utilizes **Pygame Community Edition (pygame-ce)**, which provides out-of-the-box support for modern Python interpreters.

### Installation Steps:

1. **Clone the repository or download the source code:**

   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY
   ```

2. **Install the compatible library (Pygame Community Edition):**
   ```bash
   pip install pygame-ce
   ```
   _(Note: Even though it is downloaded as `pygame-ce`, it is still imported transparently in the script using standard `import pygame`)._

---

## 🚀 How to Run

Once the dependencies are installed, simply execute the main script from your terminal or favorite code editor:

```bash
python reloj_Analogico.py
```

---

## 🧠 Technical Details & Implementation

### Coordinate Conversion (Polar to Cartesian)

To position the hour digits and draw the hands at precise circular angles, the script converts the radius (r) and angle in degrees (θ) into flat pixel coordinates (X, Y) using basic trigonometry:

```python
def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + width // 2, height // 2 - y
```

### Hand Angle Logic

- **Seconds Hand:** Rotates $6^{\circ}$ for every elapsed second ($360^{\circ} / 60$).
- **Minutes Hand:** Calculates its angle by adding a fractional shift based on the current seconds, achieving a progressive sweeping motion.
- **Hours Hand:** Adjusts its position by adding the fraction of current minutes. This ensures the hour hand moves naturally between numbers as time passes.

---

## 👤 Author

- **GitHub.com/VictorHVV** - _Desarrollo del proyecto_
