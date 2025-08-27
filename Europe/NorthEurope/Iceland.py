import matplotlib.pyplot as plt
import numpy as np

parties = ['S',	'D', 'C', 'F', 'M', 'B', 'J', 'P', 'V']
polling_2025 = [31.6, 18.6, 16.1, 6.3, 9.6, 6.3, 2.6, 4.5, 4.2]
election_2024 = [20.75,	19.36, 15.82, 13.78, 12.10, 7.80, 3.96, 3.02, 2.34]

poll_colors = ['#eb1504', '#04acec', '#f58327', '#fbcc3e', '#162069', '#04412b', '#ec4b3c', '#976dff', '#04bb7b']
election_colors = ['#f37268', '#68cdf3', '#f9b47d', '#fce08b', '#7379a5', '#688d7f', '#f3938a', '#c0a7ff', '#68d6af']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Iceland Opinion Polls')

plt.savefig('Europe/NorthEurope/Iceland Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()