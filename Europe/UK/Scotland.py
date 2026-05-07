import matplotlib.pyplot as plt
import numpy as np

parties = ['SNP', 'Con', 'Lab', 'Grn', 'LD', 'Ref']
polling_2026 = [36.0, 11.0, 17.0, 10.0, 6.0, 18.0]
election_2021 = [40.3, 23.5, 17.9, 8.1, 5.1, 0.2]

poll_colors = ['#fdf38e', '#10a9e3', '#db073d', '#16a262', '#faa61a', '#51dcee']
election_colors = ['#fdf7bb', '#6fcbee', '#e96a8a', '#73c7a0', '#fcc975', '#96eaf4']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='May 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Scotland Opinion Polls')

plt.savefig('Europe/UK/Scotland Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()