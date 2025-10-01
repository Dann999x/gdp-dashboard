import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Body na kružnici 🎯")

# Vstupy od uživatele
x0 = st.number_input("Souřadnice středu X:", value=0.0)
y0 = st.number_input("Souřadnice středu Y:", value=0.0)
r = st.number_input("Poloměr kružnice:", value=5.0, min_value=0.1)
n = st.number_input("Počet bodů:", value=10, min_value=1, step=1)
color = st.color_picker("Vyber barvu bodů:", "#ff0000")

# Výpočet souřadnic bodů
theta = np.linspace(0, 2*np.pi, int(n), endpoint=False)
x = x0 + r * np.cos(theta)
y = y0 + r * np.sin(theta)

# Vykreslení
fig, ax = plt.subplots()
ax.scatter(x, y, c=color, s=100)     # body
ax.add_artist(plt.Circle((x0, y0), r, fill=False, color="gray", linestyle="--"))  # kružnice
ax.set_aspect("equal", adjustable="box")
ax.set_title("Body na kružnici")
ax.grid(True)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Body na kružnici 🎯")

# Vstupy od uživatele
x0 = st.number_input("Souřadnice středu X:", value=0.0)
y0 = st.number_input("Souřadnice středu Y:", value=0.0)
r = st.number_input("Poloměr kružnice [m]:", value=5.0, min_value=0.1)
n = st.number_input("Počet bodů:", value=10, min_value=1, step=1)
color = st.color_picker("Vyber barvu bodů:", "#ff0000")

# Výpočet souřadnic bodů
theta = np.linspace(0, 2*np.pi, int(n), endpoint=False)
x = x0 + r * np.cos(theta)
y = y0 + r * np.sin(theta)

# Vykreslení
fig, ax = plt.subplots()
ax.scatter(x, y, c=color, s=100, label="Body na kružnici")     
ax.add_artist(plt.Circle((x0, y0), r, fill=False, color="gray", linestyle="--", label="Kružnice"))

# Osy a měřítko
ax.axhline(0, color="black", linewidth=0.5)  # osa X
ax.axvline(0, color="black", linewidth=0.5)  # osa Y
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")
ax.set_aspect("equal", adjustable="box")
ax.set_title("Body na kružnici s osami")
ax.legend()
ax.grid(True)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Body na kružnici 🎯")

# --- Sidebar: informace ---
st.sidebar.title("ℹ️ O aplikaci")
st.sidebar.markdown("""
**Autor:** Daniel Křivánek  
**Použité technologie:**  
- Python 
- Streamlit  

Tato aplikace demonstruje vykreslení bodů na kružnici 
na základě vstupních parametrů.
""")

# --- Vstupy od uživatele ---
x0 = st.number_input("Souřadnice středu X:", value=0.0)
y0 = st.number_input("Souřadnice středu Y:", value=0.0)
r = st.number_input("Poloměr kružnice [m]:", value=5.0, min_value=0.1)
n = st.number_input("Počet bodů:", value=10, min_value=1, step=1)
color = st.color_picker("Vyber barvu bodů:", "#ff0000")

# --- Výpočet souřadnic bodů ---
theta = np.linspace(0, 2*np.pi, int(n), endpoint=False)
x = x0 + r * np.cos(theta)
y = y0 + r * np.sin(theta)

# --- Vykreslení ---
fig, ax = plt.subplots()
ax.scatter(x, y, c=color, s=100, label="Body na kružnici")     
ax.add_artist(plt.Circle((x0, y0), r, fill=False, color="gray", linestyle="--", label="Kružnice"))

# Osy a měřítko
ax.axhline(0, color="black", linewidth=0.5)  
ax.axvline(0, color="black", linewidth=0.5)  
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")
ax.set_aspect("equal", adjustable="box")
ax.set_title("Body na kružnici s osami")
ax.legend()
ax.grid(True)

st.pyplot(fig)

tab1, tab2 = st.tabs(["⚙️ Aplikace", "ℹ️ O aplikaci"])

with tab1:
    # sem dáš vstupy + graf
    
with tab2:
    st.subheader("O aplikaci")
    st.write("Autor: Daniel Křivánek")
    st.write("Použité technologie: Streamlit, Matplotlib, NumPy")
