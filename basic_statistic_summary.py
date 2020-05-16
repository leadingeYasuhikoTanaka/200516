"""
基礎集計：訓練データの要約統計量確認
"""

# ライブラリのインポート
import pandas as pd

# 定数の初期化
data_folder = '.\\data\\'
train_file_name = 'train_org.csv'

train_file_path = data_folder + train_file_name

# 訓練データのロード
train = pd.read_csv(train_file_path, encoding='UTF8')
df = pd.DataFrame(train)
print(df.describe())
