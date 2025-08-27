import matplotlib.pyplot as plt
import numpy as np

parties = ['PL', 'PN', 'AD+PD', 'Momentum']
polling_2025 = [53.3, 39.7, 1.6, 3.1]
election_2022 = [55.11, 41.74, 1.61, 0.10]

poll_colors = ['#e73431', '#5087b2', '#20aa63', '#1aaa9b']
election_colors = ['#f08583', '#96b7d0', '#79cca1', '#75ccc3']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Malta Opinion Polls')

plt.savefig('Europe/SouthEurope/Malta Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()