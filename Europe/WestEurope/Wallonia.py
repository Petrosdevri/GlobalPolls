import matplotlib.pyplot as plt
import numpy as np

parties = ['MR', 'PS', 'LE', 'PTB', 'Ecolo', 'DéFI']
polling_2025 = [24.0, 25.5, 19.2, 16.8, 8.6, 3.2]
election_2024 = [28.21, 21.98, 20.01, 11.64, 6.89, 2.36]

poll_colors = ['#042df9', '#fa0404', '#06e4d2', '#8b0000', '#5eab3e', '#db047b']
election_colors = ['#6881fb', '#fc6868', '#69eee4', '#b96666', '#9ecc8b', '#e968af']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Wallonia Opinion Polls')

plt.savefig('Europe/WestEurope/Wallonia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()