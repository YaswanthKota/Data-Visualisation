import matplotlib.pyplot as plt
cases=[1251,1397,1834,2069,2547,3072,3374]
dates=['march 30','march 31','april 1','april 2','april 3','april 4','april 5']
plt.plot(cases,dates,marker='.',color='red')
plt.ylabel("Dates")
plt.xlabel("Number of corona cases in INDIA")
plt.title("COVID-19 INDIA")
plt.grid(True)
plt.show()