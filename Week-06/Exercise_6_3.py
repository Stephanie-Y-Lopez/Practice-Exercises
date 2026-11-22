#Stephanie Y. Lopez Chavoya
import statistics

days = [
    'Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday', 
    'Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday']

sales = [
    1250, 1480, 1100, 1650, 1850,
    1420, 1700, 1300, 2100, 1950]

print("DAILY SALES REPORT")
print('-' * 20)

for i in range(len(days)):
    print(f"{days[i]}: ${sales[i]:,.2f}")

mean_sales = statistics.mean(sales)
median_sales = statistics.median(sales)
mode_sales = statistics.mode(sales)
stdev_sales = statistics.stdev(sales)

print(f"The total sales amount is: {mean_sales: ,.2f}")
print(f"The median sales amount is: {median_sales: ,.2f}")
print(f"The mode sales amount is: {mode_sales: ,.2f}")
print(f"The standard deviation sales amount is: {stdev_sales: ,.2f}")

sum_sales = statistics.sum
