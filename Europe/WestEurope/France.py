import matplotlib.pyplot as plt
import numpy as np

parties = ['RN', 'NFP', 'Ensemble', 'LR', 'DVD', 'DVG']
polling_2025 = [36.0, 21.0, 18.0, 11.0, 2.0, 7.0]
election_2024 = [33.21, 28.21, 21.28, 6.57, 3.60, 1.57]

poll_colors = ['#202955', '#e00633', '#fdd01c', '#1e75d0', '#adc1fd', '#ffc0c0']
election_colors = ['#797e99', '#ec6984', '#fde276', '#78ace2', '#cdd9fd', '#ffd9d9']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('France Opinion Polls')

plt.savefig('Europe/WestEurope/France Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()