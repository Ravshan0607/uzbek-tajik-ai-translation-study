import matplotlib.pyplot as plt
import numpy as np




categories = ('word', 'slang', 'story', 'phrase')
total = (10, 3, 3, 7)

plt.bar(categories, total)
plt.title("Number of questions by category")
plt.xlabel("categories")
plt.ylabel("total")
plt.show()
