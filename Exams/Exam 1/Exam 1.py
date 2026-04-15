import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import seaborn as sns

WINDOW = 21
FACTOR = 2.326

# ----------------------- Data Ingestion ---------------------------------
df = pd.read_excel('./Indices_Download_2026.xlsx',
                   parse_dates=['Date']).set_index('Date')
df = df.loc['2025-01-01':'2026-01-15']
df = df[['^GSPC']]

# ----------------------- Question 3 -------------------------------------
# ----------------------- Question a -------------------------------------
df['return'] = np.log(df['^GSPC'] / df['^GSPC'].shift(1))
df['rolling_std'] = df['return'].rolling(WINDOW).std()
df['10_day_VaR'] = FACTOR * df['rolling_std'] * 10**0.5
df['10_day_forward_return'] = np.log(df['^GSPC'].shift(-10) / df['^GSPC'])
df = df.dropna(subset=['rolling_std', '10_day_forward_return', '10_day_VaR'])
df['breach'] = df['10_day_forward_return'] > df['10_day_VaR']
breaches = int(df['breach'].sum())

print(f'Number of VaR breaches: {breaches=}')
print(f'Percentage of breaches: {(breaches / len(df.index))=:.4f}')

# ----------------------- Question b -------------------------------------
sns.set_theme()
plt.figure(figsize=(12, 6))

sns.lineplot(data=df, x=df.index, y='10_day_VaR',
             linewidth=1.5, label='10D VaR')
sns.lineplot(data=df, x=df.index, y='10_day_forward_return',
             linewidth=1.5, label='10D Return')
breaches = df[df['breach']]
plt.scatter(breaches.index, breaches['10_day_forward_return'],
            color=sns.color_palette()[2], s=100, marker='x', zorder=5, label='Breaches')
plt.ylabel('')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------- Question c -------------------------------------
yellow_limit = binom.ppf(0.95, len(df.index), 0.01)
red_limit = binom.ppf(0.9999, len(df.index), 0.01)

print(f'Our lower bound for the yellow zone is {yellow_limit}')
print(f'Our lower bound for the red zone is {red_limit}')

# ----------------------- Question 4 -------------------------------------
# ----------------------- Question a -------------------------------------
INITIAL_VAR = df['return'].var()
LAMBDA = 0.72

df['ewma_1d_var'] = np.nan
df.loc[df.index[0], 'ewma_1d_var'] = LAMBDA * \
    INITIAL_VAR + (1-LAMBDA) * df['return'].iloc[0]**2
for i in range(1, len(df.index)):
    df.iloc[i, df.columns.get_loc('ewma_1d_var')] = LAMBDA * df['ewma_1d_var'].iloc[i-1] + \
        (1 - LAMBDA) * df['return'].iloc[i-1] ** 2
df['ewma_1d_var_check'] = (df['return']**2).ewm(alpha=1-LAMBDA).mean()
df['ewma_10_day_VaR'] = FACTOR * np.sqrt(df['ewma_1d_var']) * 10**0.5
df['ewma_breach'] = df['10_day_forward_return'] > df['ewma_10_day_VaR']
ewma_breaches = int(df['ewma_breach'].sum())

print(f'Number of EWMA VaR breaches: {ewma_breaches=}')
print(f'Percentage of EWMA breaches: {(ewma_breaches / len(df.index))=:.4f}')

# ----------------------- Question b -------------------------------------
sns.set_theme()
plt.figure(figsize=(12, 6))

sns.lineplot(data=df, x=df.index, y='ewma_10_day_VaR',
             linewidth=1.5, label='10D EWMA VaR')
sns.lineplot(data=df, x=df.index, y='10_day_forward_return',
             linewidth=1.5, label='10D Return')
ewma_breaches = df[df['ewma_breach']]
plt.scatter(ewma_breaches.index, ewma_breaches['10_day_forward_return'],
            color=sns.color_palette()[2], s=100, marker='x', zorder=5, label='Breaches')
plt.ylabel('')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
