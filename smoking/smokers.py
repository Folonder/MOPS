import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../dataset.csv', delimiter=',')
data['sex'] = data['sex'].replace({'Male': 1, 'Female': 0})
data['DRK_YN'] = data['DRK_YN'].replace({'Y': 1, 'N': 0})
# data = data[data['SMK_stat_type_cd'] == 0]
groups = data.groupby('SMK_stat_type_cd')
data = groups.get_group(1)
correlation_matrix = data.corr().round(2)

plt.figure(figsize=(8, 6))  # Размер графика
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

# Добавьте название графика
plt.title('Корреляционная матрица некурящих')

# Отобразите график
plt.show()