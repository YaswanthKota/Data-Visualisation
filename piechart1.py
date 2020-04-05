import matplotlib.pyplot as plt
labels=['Confirmed','Recovered','Deaths']
cases=[3577,285,83]
separated=(0,.1,0)
plt.pie(cases,labels=labels,autopct="%1.1f%%",explode=separated)
plt.title("COVID-19 in INDIA")
plt.axis('equal')
plt.show()