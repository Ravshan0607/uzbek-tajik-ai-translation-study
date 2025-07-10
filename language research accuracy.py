import matplotlib.pyplot as plt
import numpy as np



categories = ['word','slang','story','phrase']
accuracy = [1, 1, 0, 2]

plt.bar(categories, accuracy)
plt.title("Words by category")
plt.xlabel("categories")
plt.ylabel("accuracy")
plt.show()
