import matplotlib.pyplot as plt
import numpy as np

parties = ['Lab', 'Con', 'PC', 'Grn', 'LD', 'Ref']
polling_2026 = [15.0, 11.0, 30.0, 9.0, 6.0, 27.0]
election_2021 = [36.2, 25.1, 20.7, 4.4, 4.3, 1.1]

poll_colors = ['#db073d', '#10a9e3', '#005b54', '#16a262', '#faa61a', '#51dcee']
election_colors = ['#e96a8a', '#6fcbee', '#669c98', '#73c7a0', '#fcc975', '#96eaf4']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='May 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Wales Opinion Polls')

plt.savefig('Europe/UK/Wales Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()