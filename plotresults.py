import json
import numpy as np

import matplotlib.pyplot as plt

# Load JSON data
with open('10vus.json', 'r') as file:
    data = json.load(file)

# Extract session lengths
session_length = data['aggregate']['summaries']['vusers.session_length']
summ_lcp = data['aggregate']['summaries']['browser.page.LCP.https://en.wikipedia.org/wiki/Dog']

intermediates = data['intermediate']

j = 10
dog_times= []
cat_times = []
all_tests_times = []
absolute_timer =[] 
requests_200_percent =[] 
for i in intermediates[1:]:
    print(f"for {j} counter time is:  {i['lastMetricAt']-i['firstMetricAt']}")
    
    try:
        dog= i['summaries']["browser.step.DogPageAllSteps"]["median"]
        cat= i['summaries']["browser.step.CatPageAllSteps"]["median"]
        req_stat200= i['counters']["browser.page.codes.200"]
        req_allstat= i['counters']["browser.http_requests"]

        print(f"Percent of requests 200 stats requests {req_stat200/req_allstat*100:.3f}%")
        absolute_timer.append(j)
        dog_times.append(dog)
        cat_times.append(cat)
        requests_200_percent.append(req_stat200/req_allstat*100)
        all_tests_times.append(int(cat)+int(dog))
    except KeyError:
        pass
    j+=10


plt.plot(absolute_timer, all_tests_times, marker='s', color='#BDFC49', mfc='#9968A7', mec='#9968A7')

plt.figure(1)
plt.title('All Tests Times in Total Time (10VUs)')
plt.xlabel('Total Time [s]')
plt.ylabel('All Tests Times [ms]')

plt.figure(2)
plt.plot(absolute_timer, cat_times, marker='o', color='#49A8FC', mfc='#FF9D01', mec='#FF9D01')
plt.title('Cat Page Test Times')
plt.xlabel('Total Time [s]')
plt.ylabel('Cat Page median times [ms]')

plt.figure(3)
plt.plot(absolute_timer, dog_times, marker='*', color='#4955FC', mfc='#FCC249', mec='#FCC249')
plt.title('Dog Page Test Times')
plt.xlabel('Total Time [s]')
plt.ylabel('Dog Page Times [ms]')

plt.figure(4)
plt.plot(absolute_timer, requests_200_percent, marker='D', color='#4955FC', mfc='#FCC249', mec='#FCC249')
plt.title('Requests With 200 Status')
plt.xlabel('Total Time [s]')
plt.ylabel('200 requests partition in all requests [%]')

plt.show()

exit()
# # Plot session lengths
# # Plot LCP values as a column chart
# lcp_values = [summ_lcp[key] for key in summ_lcp]

# plt.figure(figsize=(10, 5))
# plt.bar(list(summ_lcp.keys()), lcp_values)
# plt.xlabel('Sessions')
# plt.ylabel('LCP Values')
# plt.title('LCP Values per Session')
# plt.grid(True)
# plt.show()
# # Plot session lengths as a column chart
# session_values = [session_length[key] for key in session_length]

# plt.figure(figsize=(10, 5))
# plt.bar(list(session_length.keys()), session_values)
# plt.xlabel('Sessions')
# plt.ylabel('Session Lengths')
# plt.title('Session Lengths per Session')
# plt.grid(True)
# plt.show()
# Display both charts at the same time


lcp_values = [summ_lcp[key] for key in summ_lcp]
session_values = [session_length[key] for key in session_length]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plot LCP values
#ax1.bar(list(summ_lcp.keys()), lcp_values)
ax1.set_ylabel('LCP Values')
ax1.set_title('LCP Values per Session')
ax1.grid(True)
ax1.set_facecolor('#F5F5F5')

ax2.set_ylabel('Session Lengths')
ax2.set_title('vusers.session_length')
ax2.grid(True)
ax2.set_facecolor('#F5F5F5')

# Filter LCP values for 'min' and 'max' keys
filtered_lcp_values = {key: summ_lcp[key] for key in summ_lcp if key in ['min', 'max', 'mean', 'median', 'p75', 'p95']}
filtered_lcp_keys = list(filtered_lcp_values.keys())
filtered_lcp_values = list(filtered_lcp_values.values())

# Plot filtered LCP values
ax1.bar(filtered_lcp_keys, filtered_lcp_values, color='#237569')

ax2.bar(list(session_length.keys()), session_values)


plt.tight_layout()
plt.show()