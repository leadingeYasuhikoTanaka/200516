"""
売上の日別売上高（折れ線グラフ
"""
# ライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

# 定数の初期化
data_folder = '.\\data\\'
train_file_name = 'train_org.csv'

train_file_path = data_folder + train_file_name

# 訓練データのロード
train = pd.read_csv(train_file_path, encoding='UTF8')

X = train['datetime']
Y = train['y']
# print(X, Y)

fig, ax = plt.subplots()
ax.plot(X, Y)
plt.show()
