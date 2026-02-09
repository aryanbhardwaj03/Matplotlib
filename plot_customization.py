import matplotlib.pyplot as plt
import numpy as np

x=np.array([2023,2024,2025,2026])
y1=np.array([15,30,45,50])
y2=np.array([17,23,38,5])
y3=np.array([13,15,20,35])

plt.plot(x,y1, marker=".",markersize=30, markerfacecolor ="#005eff", markeredgecolor = "#000000",linestyle="solid", linewidth=4, color="#8B4513")
plt.plot(x,y2, marker =".", markersize=30, markerfacecolor ="#FF0000", markeredgecolor = "#000000",linestyle="solid", linewidth=4, color="#D9FF00")
plt.plot(x,y3,marker=".", markersize=30, markerfacecolor ="#00FF00", markeredgecolor = "#000000",linestyle="solid", linewidth=4, color="#5900FF")
plt.show()

