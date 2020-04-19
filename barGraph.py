import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import readFiles as rf
import datetime

#json読み込み 
json = rf.readJsonFile('japan.json')

leftList = list()
deathsList = list()
recoveredList = list()
activeList = list()


#jsonをリストに変換
for dailyData in json:
    leftList.append(datetime.datetime.strptime(dailyData["Date"], '%Y-%m-%dT%H:%M:%SZ'))
    deathsList.append(dailyData["Deaths"])
    recoveredList.append(dailyData["Recovered"])
    activeList.append(dailyData["Confirmed"] - dailyData["Recovered"] - dailyData["Deaths"])

left = np.asarray(leftList)
deaths = np.asarray(deathsList)
recovered = np.asarray(recoveredList)
active = np.asarray(activeList)

#棒グラフでプロット
plt.title("total number of infected and deaths in Japan")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.grid(True)
p1 = plt.bar(left, deaths, color="gray")
p2 = plt.bar(left, recovered, bottom=deaths, color="green")
p3 = plt.bar(left, active, bottom=recovered, color="blue")
plt.legend((p1[0], p2[0], p3[0]), ("deaths", "recovered", "active"))

#get current axes
ax = plt.gca()
 
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.show()