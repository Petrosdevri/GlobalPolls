import matplotlib.pyplot as plt
import numpy as np

parties = ['MR-Open VLD', 'PS-Vooruit', 'PTB/PvdA', 'Ecolo-Groen', 'Les Engagés-CD&V', 'DéFI', 'TFA', 'N-VA', 'VB']
polling_2025 = [23.1, 23.8, 18.7, 9.8, 9.7, 3.2, 2.5, 0.1, 0.1]
election_2024 = [23.15, 18.60, 16.75, 11.30, 9.52, 6.58, 4.78, 2.79, 2.46]

poll_colors = ['#042df9', '#fa0404', '#7f0000', '#5eab3e', '#06e4d2', '#db047b', '#5d18e9', '#fcbb27', '#fee600']
election_colors = ['#6881fb', '#fc6868', '#b26666', '#9ecc8b', '#69eee4', '#e968af', '#9d74f1', '#fdd67d', '#fef066']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Belgium Opinion Polls')

plt.savefig('Europe/WestEurope/Belgium Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()