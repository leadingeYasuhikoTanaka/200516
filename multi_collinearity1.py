"""
多重共線性のチェック：対象は説明変数の候補全部
"""

# ライブラリのインポート
import pandas as pd

# 定数の初期化
data_folder = '.\\data\\'
train_file_name = 'train_org.csv'

train_file_path = data_folder + train_file_name

# 訓練データのロード
train = pd.read_csv(train_file_path, encoding='UTF8')

# 多重共線性確認
df1 = pd.DataFrame(train)
df2 = df1.drop('y', axis=1)
print(df2.corr())
