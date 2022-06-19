import csv
from datetime import datetime
from matplotlib import pyplot as plt

file1 = "sitka_weather_2014.csv"
file2 = 'death_valley_2014.csv'

with open(file1) as f1, open(file2) as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    next(reader1)
    next(reader2)

    sitka_dates, sitka_highs, dv_dates, dv_highs = [], [], [], []

    for row in reader1:
        try:
           current_date = datetime.strptime(row[0], "%Y-%m-%d")
           sitka_high = int(row[1])
        except ValueError:
            print(current_date, "Missing Date")
        else: 
            sitka_dates.append(current_date)
            sitka_highs.append(sitka_high)

    for row in reader2:
        try:
           current_date2 = datetime.strptime(row[0], "%Y-%m-%d") 
           dv_high = int(row[1])
        except ValueError:
            print(current_date2, "Missing Date")
        else:
            dv_dates.append(current_date2)
            dv_highs.append(dv_high)
    
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(sitka_dates, sitka_highs, c='red', alpha=0.5, label='Sitka Highs')
    plt.plot(dv_dates, dv_highs, c='green', alpha=0.5, label='Death Valley Highs')
    
    plt.title("Daily temperatures, July 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.legend()
    plt.show()
