import matplotlib.pyplot as plt
import numpy as np

parties = ['CDU', 'SPD', 'Grüne', 'Linke', 'AfD', 'FDP', 'BSW']
polling_2026 = [18.8, 12.1, 14.3, 25.7, 16.3, 2.5, 4.7]
election_2026 = [28.23, 18.39, 18.39, 12.20, 9.09, 4.64, 0.10]

poll_colors = ['#202020', '#e00510', '#479743', '#be3075', '#44b4e6', '#ffec01', '#7b1e50']
election_colors = ['#797979', '#ec696f', '#90c08e', '#d882ac', '#8ed2f0', '#fff366', '#af7896']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='September 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Berlin Opinion Polls')

plt.savefig('Europe/WestEurope/Berlin Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()