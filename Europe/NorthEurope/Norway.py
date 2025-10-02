import matplotlib.pyplot as plt
import numpy as np

parties = ['Ap', 'H', 'Sp', 'FrP', 'SV', 'R', 'V', 'MDG', 'KrF']
polling_2025 = [27.2, 14.5, 5.9, 20.9, 6.0, 6.0, 4.3, 6.1, 4.7]
election_2021 = [26.25, 20.35, 13.50, 11.61, 7.64, 4.72, 4.61, 3.94, 3.80]

poll_colors = ['#e01927', '#0365f1', '#01853d', '#014f81', '#b5317c', '#e80202', '#016667', '#5c961d', '#fdef32']
election_colors = ['#ec757d', '#67a2f6', '#66b58a', '#6695b3', '#d283b0', '#f16767', '#66a3a3', '#9dc077', '#fdf584']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Norway Opinion Polls')

plt.savefig('Europe/NorthEurope/Norway Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()