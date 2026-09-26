import matplotlib.pyplot as plt
import numpy as np

parties = ['PB', 'GERB-SDS', 'PP-DB', 'DPS-NN', 'Vazrazdhane', 'MECh', 'Velichie', 'BSP-OL']
polling_2026 = [44.4, 12.6, 14.6, 7.4, 5.0, 2.2, 2.3, 3.7]
election_2026 = [44.59, 13.39, 12.62, 7.12, 4.26, 3.23, 3.10, 3.02]

poll_colors = ['#204a41', '#2269b9', '#0818f0', '#0c62a1', '#bc9f6b', '#000000', '#ad3537', '#d21c26']
election_colors = ['#62807a', '#7aa5d5', '#6a74f6', '#6da0c6', '#d6c5a6', '#666666', '#cd8587', '#e4767c']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='September 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Bulgaria Opinion Polls')

plt.savefig('Europe/SouthEurope/Bulgaria Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()