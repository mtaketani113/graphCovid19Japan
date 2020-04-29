"""日本の感染者の推移を棒グラフで表示する."""
import numpy as np
import matplotlib.pyplot as plt
import readfiles as rf

# json読み込み
json = rf.read_json_file('japan.json')

# 末尾2つのデータは不要なので削除
json.pop(-1)
json.pop(-1)

plotData = json[-1]

# 円グラフでプロット
label = ['active', 'recovered', 'deaths']
active_number = plotData["Confirmed"] - plotData["Recovered"] - plotData["Deaths"]
x = np.array([active_number, plotData["Recovered"], plotData["Deaths"]])
plt.pie(x, labels=label, counterclock=False, startangle=90)
plt.axis('equal')

plt.show()
