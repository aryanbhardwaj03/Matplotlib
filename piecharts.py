import matplotlib.pyplot as plt
import numpy as np

# Bar chart = circular chart divided into slices to show percentages of the total.
#             Good for visualizing distribuion among categories.

categories = ["Freshmen", "Sophmores","Juniors","Seniors"]
values = np.array([300,250,275,225])
colors=["red","yellow","blue","green"]
plt.pie(values,labels=categories, autopct = "%1.1f%%", colors=colors, explode=[0,0,0,0.2], shadow = True, startangle = 90)
plt.title("Aryan Bhardwaj USAR")

plt.show()