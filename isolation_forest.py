import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = np.random.randint(90, 110, size=1000)
outliers = np.random.randint(140, 170 , size =24)
plt.scatter(data[0:499], data[500:999], )

plt.show()
data = np.append(data, outliers)
outliers = np.random.randint(40, 70, size=25)
glucose_readings = pd.DataFrame(data, columns = ['glucose_levels'])

print(glucose_readings)