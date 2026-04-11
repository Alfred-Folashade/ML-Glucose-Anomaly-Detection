import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = np.random.randint(90, 110, size=100)
outliers = np.random.randint(140, 170 , size =24)

data = np.append(data, outliers)
plt.scatter(data[0:62], data[62:125], )
plt.show()
outliers = np.random.randint(40, 70, size=25)
glucose_readings = pd.DataFrame(data, columns = ['glucose_levels'])

print(glucose_readings)