import matplotlib.pyplot as plt
import numpy as np

parties = ['NAT', 'LAB', 'GRN', 'ACT', 'NZF', 'TPM', 'TOP']
polling_2025 = [32.9, 33.3, 9.9, 8.3, 8.4, 3.5, 2.0]
election_2022 = [38.08, 26.92, 11.61, 8.64, 6.09, 3.08, 2.22]

poll_colors = ['#338ccc', '#dc2c24', '#04b43c', '#fbdc04', '#241c1c', '#d42c3b', '#0ab39a']
election_colors = ['#84bae0', '#ea807b', '#68d28a', '#fcea68', '#7b7676', '#e58089', '#6cd1c2']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('New Zealand Opinion Polls')

plt.savefig('Oceania/Asia-Pacific/New Zealand Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()