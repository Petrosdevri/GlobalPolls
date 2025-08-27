import matplotlib.pyplot as plt
import numpy as np

parties = ['JV', 'ZZS', 'AS', 'NA', 'ST!', 'LPV', 'PRO', 'KP', 'LA', 'S']
polling_2025 = [11.5, 10.4, 10.6, 15.4, 5.1, 14.0, 11.6, 1.8, 2.5, 4.0]
election_2022 = [18.92, 12.40, 10.98, 9.27, 6.78, 6.22, 6.14, 4.96, 4.96, 4.76]

poll_colors = ['#6bb646', '#015f2a', '#ffac01', '#942130', '#f77c03', '#9e3138', '#f93822', '#fef201', '#ffdd00', '#ef1c27']
election_colors = ['#a6d390', '#669f7f', '#ffcd66', '#be7982', '#fab067', '#c48387', '#fb877a', '#fef766', '#ffea66', '#f5767d']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Latvia Opinion Polls')

plt.savefig('Europe/NorthEurope/Latvia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()