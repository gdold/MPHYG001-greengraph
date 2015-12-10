import matplotlib.pyplot as plt
from graph import Greengraph

mygraph=Greengraph('New York','Chicago')
data = mygraph.green_between(20)
plt.plot(data)
plt.show()