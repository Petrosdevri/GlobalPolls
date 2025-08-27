import matplotlib.pyplot as plt
import numpy as np

parties = ['LSDP', 'TS-LKD', 'PPNA', 'DSVL', 'LS', 'LVŽS', 'LP', 'LLRA-KŠS']
polling_2025 = [15.5, 19.7, 5.2, 14.1, 10.5, 9.3, 6.2, 3.8]
election_2024 = [19.70, 18.35, 15.26, 9.40, 7.85, 7.16, 4.62, 3.96]

poll_colors = ['#e10514', '#00a59b', '#ea602b', '#0b1072', '#ff9300', '#01a650', '#e50161', '#761724']
election_colors = ['#ed6972', '#66c9c3', '#f29f7f', '#6c6faa', '#ffbe66', '#66c996', '#ef66a0', '#ac737b']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Lithuania Opinion Polls')

plt.savefig('Europe/NorthEurope/Lithuania Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()