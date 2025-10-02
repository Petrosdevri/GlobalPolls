import matplotlib.pyplot as plt
import numpy as np

parties = ['Lab', 'Con', 'Ref', 'LD', 'Grn', 'SNP']
polling_2025 = [19.0, 16.0, 32.0, 14.0, 9.0, 2.0]
election_2024 = [33.7, 23.7, 14.3, 12.2, 6.4, 2.5]

poll_colors = ['#db073d', '#10a9e3', '#51dcee', '#faa61a', '#16a262', '#fdf38e']
election_colors = ['#e96a8a', '#6fcbee', '#96eaf4', '#fcc975', '#73c7a0', '#fdf7bb']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('UK Opinion Polls')

plt.savefig('Europe/UK/UK Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()