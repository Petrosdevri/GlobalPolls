import matplotlib.pyplot as plt
import numpy as np

parties = ['SPD', 'AfD', 'CDU', 'Linke', 'Grüne', 'FDP', 'BSW']
polling_2026 = [35.5, 38.2, 4.9, 6.5, 5.7, 1.0, 4.8]
election_2026 = [39.59, 16.72, 13.30, 9.94, 6.30, 5.80, 0.10]

poll_colors = ['#e00510', '#44b4e6', '#202020', '#be3075', '#479743', '#ffec01', '#7b1e50']
election_colors = ['#ec696f', '#8ed2f0', '#797979', '#d882ac', '#90c08e', '#fff366', '#af7896']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='September 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Mecklenburg-Vorpommern Opinion Polls')

plt.savefig('Europe/WestEurope/Mecklenburg-Vorpommern Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()