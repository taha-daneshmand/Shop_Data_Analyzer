import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# columns: 'product_id', 'category', 'price', 'quantity_sold', 'date'
df = pd.read_csv('digikala_sales.csv')

print(df.head())

df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('توزیع قیمت‌ها')
plt.xlabel('قیمت')
plt.ylabel('تعداد')
plt.show()

category_sales = df.groupby('category')['quantity_sold'].sum().reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='quantity_sold', y='category', data=category_sales)
plt.title('مجموع فروش بر اساس دسته‌بندی')
plt.xlabel('تعداد فروش')
plt.ylabel('دسته‌بندی')
plt.show()

daily_sales = df.groupby('date')['quantity_sold'].sum().reset_index()
plt.figure(figsize=(14, 8))
sns.lineplot(x='date', y='quantity_sold', data=daily_sales)
plt.title('روند فروش روزانه')
plt.xlabel('تاریخ')
plt.ylabel('تعداد فروش')
plt.show()

top_products = df.groupby('product_id')['quantity_sold'].sum().nlargest(10).reset_index()
top_products = pd.merge(top_products, df[['product_id', 'category']], on='product_id').drop_duplicates()
plt.figure(figsize=(14, 8))
sns.barplot(x='quantity_sold', y='product_id', hue='category', data=top_products)
plt.title('10 محصول پرفروش')
plt.xlabel('تعداد فروش')
plt.ylabel('شناسه محصول')
plt.show()