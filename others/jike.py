import pandas as pd
import numpy as np

df = pd.read_csv("")
# # from xgboost import XGBRegressor
# # from sklearn.model_selection import train_test_split
# # from sklearn.metrics import mean_squared_error

# # データの読み込み
# data = pd.read_csv('data.csv')
# data['Date'] = pd.to_datetime(data['Date'])
# data.set_index('Date', inplace=True)

# # 特徴量の作成
# def create_features(data, lag=1):
#     df = data.copy()
#     for i in range(1, lag + 1):
#         df[f'lag_{i}'] = df['Value'].shift(i)
#     return df.dropna()

# lag = 5
# data_lagged = create_features(data, lag=lag)
# X = data_lagged.drop('Value', axis=1)
# y = data_lagged['Value']

# # データの分割
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# # モデルの訓練
# model = XGBRegressor(objective='reg:squarederror', n_estimators=1000)
# model.fit(X_train, y_train)

# # 予測
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print(f'Mean Squared Error: {mse}')


