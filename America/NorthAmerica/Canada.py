import matplotlib.pyplot as plt
import numpy as np

parties = ['LPC', 'CPC', 'BQ', 'NDP', 'GPC', 'PPC']
polling_2025 = [43.5, 35.6, 6.0, 9.5, 2.6, 2.1]
election_2025 = [43.76, 41.31, 6.29, 6.29, 1.22, 0.70]

poll_colors = ['#d31c22', '#1e2d4b', '#51a5e1', '#ed7c05', '#24a044', '#64349c']
election_colors = ['#e4767a', '#788193', '#96c9ed', '#f4b069', '#7bc68e', '#a285c3']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2025, width=width, color=election_colors, label='2025 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Canada Opinion Polls')

plt.savefig('America/NorthAmerica/Canada Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()