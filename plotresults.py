import json
import numpy as np

import matplotlib.pyplot as plt

# Load JSON data
with open('artout02.json', 'r') as file:
    data = json.load(file)

# Extract session lengths
session_length = data['aggregate']['summaries']['vusers.session_length']
summ_lcp = data['aggregate']['summaries']['browser.page.LCP.https://en.wikipedia.org/wiki/Dog']

intermediates = data['intermediate']

j =0 
for i in intermediates:
    print(f"for {j} counter time is:  {i['lastMetricAt']-i['firstMetricAt']}")
    j+=1


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
ax1.set_xlabel('Sessions')
ax1.set_ylabel('LCP Values')
ax1.set_title('LCP Values per Session')
ax1.grid(True)
ax1.set_facecolor('#F5F5F5')

ax2.set_xlabel('Sessions')
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