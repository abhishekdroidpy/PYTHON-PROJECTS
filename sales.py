import numpy as np

sales=np.array([[1200,3000,2000,2500],
                             [1500,2400,5000,2000],
                              [2000,2400,2500,2800],
                              [1000,1280,2300,2200]])
                              
total_sales=np.sum(sales,axis=1)
monthly_rev=np.sum(sales,axis=0)
max_sales=np.max(total_sales)

avg_sales=np.mean(sales)
month_low=sales[sales<avg_sales]

print("total sales:",total_sales,"\n","monthly revenue:",monthly_rev,"\n","maximum sales:",max_sales,"\n",
"low performing:",month_low)