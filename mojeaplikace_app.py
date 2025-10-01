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

st.pyplot(fig)
