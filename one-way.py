from math import sqrt
from scipy.stats import t
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import f
import pprint

data = [[4.8, 5.2, 5.2, 5.4], [4.2, 4.5, 4.9, 5.9], [4.6, 4.8, 5.5, 6.2], [4.4, 5.1, 5.4, 5.7]]
df = pd.DataFrame(data, columns=["A1", "A2", "A3", "A4"])
ndarray = df.values
df
# df.transpose()

sns.set()
sns.set_style('whitegrid')
sns.set_palette('gray')
plt.hist(ndarray)
plt.show()
"""数値計算はndarrayでするべき"""
print(ndarray)
plt.boxplot(ndarray)
plt.show()

"""代表値の取得"""
df.describe().transpose()
"""修正項"""
CT = df.sum().sum()**2/df.size
"""総平方和"""
T = np.sum(ndarray**2)
St = T - CT
ft = df.size-1
print("総平方和="+str(St), "自由度="+str(ft))
"""要因平方和"""
A = ((df.sum()**2)/df.count()).sum()
Sa = A - CT
fa = len(df.columns)-1
Va = Sa/fa
print("要因平方和="+str(Sa), "自由度="+str(fa))
"""残差平方和"""
Se = St - Sa
fe = ft - fa
Ve = Se/fe
print("残差平方和="+str(Se), "自由度="+str(fe))
Fo = Va/Ve
p = (Sa-fa*Ve)/St * 100
"""分散分析表"""
clm = ["S", "f", "Variance", "Fo", "p"]
indexs = ["A", "e", "T"]
df_table = [[Sa, fa, Va, Fo, p], [Se, fe, Ve, np.nan, 100-p], [Sa+Se, fa+fe, np.nan, np.nan, 100]]
pd.options.display.precision=2
five = f.ppf(0.95, fa, fe)
print("F5=" + str(five))
pd.DataFrame(df_table, index=indexs, columns=clm)

"""平均の推定"""
df.sum()
a=0.95
t_value = t(fe).ppf((0.95+1)/2)
m_low = df.mean() - t_value*np.sqrt(Ve/df.count())
m_high = df.mean() + t_value*np.sqrt(Ve/df.count())
r = m_high-m_low

pd.options.display.precision=4
plt.errorbar(df.columns, df.mean(), r, fmt="ro", capsize=4, ecolor="black")
plt.show()
