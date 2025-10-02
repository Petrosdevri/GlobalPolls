import matplotlib.pyplot as plt
import numpy as np

parties = ['PAS', 'BEP', 'PN', 'BeA']
polling_2025 = [40.6, 28.8, 8.5, 9.0]
election_2021 = [52.80, 27.17, 4.10, 1.20]

poll_colors = ['#ffdd00', '#b91502', '#2582fa', '#026d56']
election_colors = ['#ffea66', '#d57267', '#7cb4fc', '#67a799']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Moldova Opinion Polls')

plt.savefig('Eurasia/EasternEurope/Moldova Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()