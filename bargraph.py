"""日本の感染者の推移を棒グラフで表示する."""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import readfiles as rf
import datetime as dt

# json読み込み
json = rf.read_json_file('japan.json')

# 末尾2つのデータは不要なので削除
json.pop(-1)
json.pop(-1)

left_list = list()
deaths_list = list()
recovered_list = list()
active_list = list()


# jsonをリストに変換
for daily in json:
    left_list.append(dt.datetime.strptime(daily["Date"], '%Y-%m-%dT%H:%M:%SZ'))
    deaths_list.append(daily["Deaths"])
    recovered_list.append(daily["Recovered"])
    # 感染者全体から死者と回復者を引き、闘病数を計算
    active_number = daily["Confirmed"] - daily["Recovered"] - daily["Deaths"]
    active_list.append(active_number)

left = np.asarray(left_list)
deaths = np.asarray(deaths_list)
recovered = np.asarray(recovered_list)
active = np.asarray(active_list)

# 棒グラフでプロット
plt.title("total number of infected and deaths in Japan")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.grid(True)
p1 = plt.bar(left, deaths, color="gray")
p2 = plt.bar(left, recovered, bottom=deaths, color="green")
p3 = plt.bar(left, active, bottom=recovered, color="blue")
plt.legend((p1[0], p2[0], p3[0]), ("deaths", "recovered", "active"))

# get current axes
ax = plt.gca()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.show()
