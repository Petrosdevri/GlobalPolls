import matplotlib.pyplot as plt
import numpy as np

parties = ['JV', 'ZZS', 'PRO', 'AS', 'NA', 'ST!', 'LPV', 'LA', 'S', 'SV']
polling_2026 = [6.8, 6.5, 10.2, 22.7, 8.7, 3.1, 13.3, 3.7, 2.4, 14.1]
election_2022 = [18.97, 12.44, 11.13, 11.01, 9.29, 6.80, 6.24, 4.96, 4.81, 0.10]

poll_colors = ['#6bb646', '#015f2a', '#f93822', '#ffac01', '#942130', '#f77c03', '#9e3138', '#ffdd00', '#ef1c27', '#615cb3']
election_colors = ['#a6d390', '#669f7f', '#fb877a', '#ffcd66', '#be7982', '#fab067', '#c48387', '#ffea66', '#f5767d', '#908cc9']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='September 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Latvia Opinion Polls')

plt.savefig('Europe/NorthEurope/Latvia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()