import numpy as np
import pandas as pd

data = np.random.randint(90, 110, size=1000)
glucose_readings = pd.DataFrame(data, columns = ['glucose_levels'])
print(glucose_readings)