"""
　タイトル：弁当の需要予測モデル（重回帰分析）
　目的変数：日次売上高（y）
　説明変数：　2013/11/18からの経過日数（date_diff）
            曜日区分（week_flg）
            お楽しみメニュー有無(remark_flg)
            天候区分（weather_flg）
"""
# ライブラリのインポート
import pandas as pd
from sklearn.linear_model import LinearRegression as LR

# 定数の初期化
data_folder = '.\\data\\'
train_file_name = 'm_reg_train3.csv'
test_file_name = 'm_reg_test3.csv'
# submit_file_name = 'm_regs_submit3.csv'
# submit_file_name = 'm_regs_submit4.csv'
# submit_file_name = 'm_regs_submit5.csv'
submit_file_name = 'm_regs_submit6.csv'

train_file_path = data_folder + train_file_name
test_file_path = data_folder + test_file_name
submit_file_path = data_folder + submit_file_name

# 訓練データのロード
train = pd.read_csv(train_file_path, encoding='UTF8')
# print(train)

# 評価データのロード
test = pd.read_csv(test_file_path, encoding='UTF8')
# print(test)

# 前処理済後の訓練データ（説明変数）の読み込み
X_train = train[
    ['year','month', 'week_flg', 'remarks_flg', 'weather_flg']
    # ['year','month', 'week_flg', 'remarks_flg', 'weather_flg', 'temperature']
    # ['date_diff', 'week_flg', 'remarks_flg', 'weather_flg', 'temperature']
    # ['date_diff', 'week_flg', 'remarks_flg', 'weather_flg']
]
# print(type(X_train))

# 訓練データ（目的変数）の読み込み
y_train = train['y']
# print(y_train)

# 学習
model = LR()
model.fit(X_train, y_train)

# モデルの内容確認
# 偏回帰係数とy切片と決定係数
print(model.coef_)
print(model.intercept_)
print(model.score(X_train, y_train))

# 検証用データ
X_test = test[
    ['year','month', 'week_flg', 'remarks_flg', 'weather_flg']
    # ['year','month', 'week_flg', 'remarks_flg', 'weather_flg', 'temperature']
    # ['date_diff', 'week_flg', 'remarks_flg', 'weather_flg', 'temperature']
    # ['date_diff', 'week_flg', 'remarks_flg', 'weather_flg']
]
# print(X_test)

# 予測
pred = model.predict(X_test)
print(pred)
#
# 結果ファイル作成
target = pd.DataFrame(index=[], columns=[])
target[0] = test['datetime']
target[1] = pred
target.to_csv(submit_file_path, header=None, index=None)
