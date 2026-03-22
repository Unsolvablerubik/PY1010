# Del a)
#------------------------------

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data
filename = "support_uke_24.xlsx"
data = pd.read_excel(filename)
# print(data)

# Extract columns
u_dag = data["Ukedag"].values
# print(u_dag)
kl_sett = data["Klokkeslett"].values
# print(kl_sett)
varighet = data["Varighet"].values
# print(varighet)
score = data["Tilfredshet"].values
# print(score)

#%%
# Del b)
#------------------------------

# Count occurrences of each day
count_u_dag = data['Ukedag'].value_counts()
# print(count_u_dag)

# Create column chart
plt.figure(1)  # First figure
plt.bar(count_u_dag.index, count_u_dag.values)
plt.title('Antall henvendelser per ukedag')
plt.ylabel('Antall henvendelser')
plt.show() # Show answer

# Del c)
#------------------------------

# Find min and max call durations
min_varighet = np.min(varighet)
print(f"Den minste samtaletiden er: {min_varighet}") # Show answer
max_varighet = np.max(varighet)
print(f"Den lengste samtaletiden er: {max_varighet}") # Show answer

# Del d)
#------------------------------

# Convert time strings to seconds for calculations
varighet_second = []
for time in varighet:
    h, m, s = time.split(':')
    total_second = int(h)*60*60 + int(m)*60 + int(s)
    varighet_second.append(total_second)
# print(varighet_second)

# Convert to numpy array
varighet_second = np.array(varighet_second)
# print(varighet_second)

# Calculate average
average_varighet = np.mean(varighet_second)
# print(average_varighet)

# Convert to minutes and seconds
avg_minute = int(average_varighet // 60)
avg_second = int(average_varighet % 60)
print(f"Gjennomsnittlig samtaletid: {avg_minute} minutter og {avg_second} sekunder") # Show answer

# Del e)
#------------------------------

# Extract hours from time strings
kl_sett_hour = []
for time in kl_sett:
    h, m, s = time.split(':')
    kl_sett_hour.append(int(h))
# print(kl_sett_hour)

kl_sett_hour = np.array(kl_sett_hour)
# print(kl_sett_hour)

# Count calls in each time interval
interval_counts = [0, 0, 0, 0]  # 08-10, 10-12, 12-14, 14-16
for hour in kl_sett_hour:
    if 8 <= hour < 10:
        interval_counts[0] += 1
    elif 10 <= hour < 12:
        interval_counts[1] += 1
    elif 12 <= hour < 14:
        interval_counts[2] += 1
    elif 14 <= hour < 16:
        interval_counts[3] += 1
# print(interval_counts)

# Create pie chart
intervals = ['08-10', '10-12', '12-14', '14-16']
plt.figure(2)  # Second figure
plt.pie(interval_counts, labels=intervals)
plt.title('Antall henvendelser per timeinterval')
plt.show() # Show answer

# Del f)
#------------------------------

# print(score)

# Remove NaN values
score_clean = score[~np.isnan(score)]
# print(score_clean)

# Count scores
count_score = len(score_clean)

# Count scores in each range
range_1_6 = 0
range_7_8 = 0  
range_9_10 = 0

for score in score_clean:
    if 1 <= score <= 6:
        range_1_6 += 1
    elif 7 <= score <= 8:
        range_7_8 += 1
    elif 9 <= score <= 10:
        range_9_10 += 1

# Calculate percentages
percent_promoter = (range_9_10 / count_score) * 100
percent_passive = (range_7_8 / count_score) * 100
percent_detractor = (range_1_6 / count_score) * 100

# print(percent_promoter)
# print(percent_passive)
# print(percent_detractor)

# Calculate NPS
nps = percent_promoter - percent_detractor
print("NPS = " + str(round(nps, 2)) + " %") # Show answer

