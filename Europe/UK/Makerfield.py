import matplotlib.pyplot as plt
import numpy as np

parties = ['Lab', 'Ref', 'Con', 'LD', 'Grn', 'RB']
polling_2026 = [46.0, 39.0, 2.0, 2.0, 3.0, 7.0]
election_2026 = [45.2, 31.8, 10.9, 6.8, 4.4, 0.1]

poll_colors = ['#db073d', '#51dcee', '#10a9e3', '#faa61a', '#16a262', '#011033']
election_colors = ['#e96a8a', '#96eaf4', '#6fcbee', '#fcc975', '#73c7a0', '#666f84']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='June 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Makerfield Opinion Polls')

plt.savefig('Europe/UK/Makerfield Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()