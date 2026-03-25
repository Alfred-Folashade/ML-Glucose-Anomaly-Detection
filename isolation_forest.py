import numpy as np
import pandas as pd

data = np.random.randint(90, 110, size=1000)
outliers = np.random.randint(140, 170 , size =25)
data = np.append(data, outliers)
outliers = np.random.randint(40, 70, size=25)
glucose_readings = pd.DataFrame(data, columns = ['glucose_levels'])

print(glucose_readings)