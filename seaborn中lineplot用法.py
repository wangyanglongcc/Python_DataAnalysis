import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False
rs = np.random.RandomState(365)
values = rs.randn(365, 7).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D","E","F","G"])

f, ax = plt.subplots(figsize=(16, 6))
# sns.lineplot一次最多支持6个类别
sns.lineplot(data=data.drop('G',1), palette="tab10", linewidth=2.5);
