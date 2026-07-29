import matplotlib.pyplot as plt
import numpy as np

parties = ['Lab', 'Con', 'Ref', 'Grn', 'LD', 'RB']
polling_2026 = [39.0, 12.0, 19.0, 14.0, 8.0, 8.0]
election_2026 = [63.4, 10.4, 7.5, 6.9, 4.2, 0.1]

poll_colors = ['#db073d', '#10a9e3', '#51dcee', '#16a262', '#faa61a', '#011033']
election_colors = ['#e96a8a', '#6fcbee', '#96eaf4', '#73c7a0', '#fcc975', '#666f84']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='July 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Manchester Opinion Polls')

plt.savefig('Europe/UK/Manchester Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()