"""
基礎集計：説明変数の多重共線性の確認
"""

# ライブラリのインポート
import pandas as pd
import pprint

# 定数の初期化
data_folder = '.\\data\\'
train_file_name = 'm_reg_train3.csv'

train_file_path = data_folder + train_file_name

# 訓練データのロード
train = pd.read_csv(train_file_path, encoding='UTF8')

# 多重共線性確認
df1 = pd.DataFrame(train)
df2 = df1.drop('y', axis=1)
pd.set_option('display.max_rows', 100)
print(df2.corr())
df2.corr().to_csv('.\\aaa.csv',index=None)
