import matplotlib.pyplot as plt
import numpy as np

parties = ['Union',	'AfD', 'SPD', 'Grüne', 'Linke', 'BSW', 'FDP']
polling_2025 = [25.3, 25.3, 14.3, 11.2, 11.0, 3.8, 3.2]
election_2025 = [28.52, 20.80, 16.41, 11.61, 8.77, 4.97, 4.33]

poll_colors = ['#202020', '#44b4e6', '#e00510', '#479743', '#be3075', '#7b1e50', '#ffec01']
election_colors = ['#797979', '#8ed2f0', '#ec696f', '#90c08e', '#d882ac', '#af7896', '#fff366']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2025, width=width, color=election_colors, label='2025 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('France Opinion Polls')

plt.savefig('Europe/WestEurope/Germany Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()