import matplotlib.pyplot as plt
import numpy as np

parties = ['CDU', 'AfD', 'Linke', 'SPD', 'FDP', 'Grüne', 'BSW']
polling_2026 = [18.5, 44.5, 9.4, 8.2, 2.1, 8.9, 5.0]
election_2026 = [37.12, 20.82, 10.99, 8.41, 6.42, 5.94, 0.10]

poll_colors = ['#202020', '#44b4e6', '#be3075', '#e00510', '#ffec01', '#479743', '#7b1e50']
election_colors = ['#797979', '#8ed2f0', '#d882ac', '#ec696f', '#fff366', '#90c08e', '#af7896']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='September 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Saxony-Anhalt Opinion Polls')

plt.savefig('Europe/WestEurope/Saxony-Anhalt Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()