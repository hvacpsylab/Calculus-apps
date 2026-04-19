import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.image("BITS_Logo.png", width=150)

st.title("📦 Open Box Volume Explorer")

st.write("Cut squares of size x from a 14 × 22 sheet and fold into a box.")

# Slider for x
x = st.slider("Cut size (x)", 0.1, 6.9, 3.0)

# Dimensions
length = 22 - 2*x
width = 14 - 2*x
height = x

# Volume function
V = x * length * width

st.subheader("📐 Box Dimensions")
st.write(f"Length = {length:.2f}")
st.write(f"Width = {width:.2f}")
st.write(f"Height = {height:.2f}")

st.subheader("📊 Volume")
st.write(f"Volume = {V:.2f} cubic units")

# Graph
x_vals = np.linspace(0, 7, 200)
V_vals = x_vals * (22 - 2*x_vals) * (14 - 2*x_vals)

# Find maximum (analytical approx)
x_max = 2.7854
V_max = x_max * (22 - 2*x_max) * (14 - 2*x_max)

fig, ax = plt.subplots()
ax.plot(x_vals, V_vals, label="V(x)")
ax.scatter(x, V, label="Current x")
ax.scatter(x_max, V_max, label="Maximum", marker="x", s=100)

ax.set_xlabel("x")
ax.set_ylabel("Volume")
ax.set_title("Volume vs x")
ax.legend()

st.pyplot(fig)

st.info("👉 Notice: Volume increases, reaches a maximum, then decreases.")