import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ['Телефон', 'Планшет', 'Ноутбук', 'Наушники', 'Телевизор', ]
sales_data = np.random.randint(10, 100,
                               size=(len(products), 12))


sales_df = pd.DataFrame(sales_data,
                        index=products, columns=[f'Месяц {i+1}' for i in range(12)])


sales_df.T.plot(kind='line', figsize=(25, 75))
plt.title('Продажи товаров по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество продаж')
plt.grid(True)
plt.legend(title='Товары')
plt.show()


print('Статистика продаж:\n',
      sales_df.describe())
