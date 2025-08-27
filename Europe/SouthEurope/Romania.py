import matplotlib.pyplot as plt
import numpy as np

parties = ['PSD', 'AUR', 'PNL', 'USR', 'SOS', 'POT', 'UDMR']
polling_2025 = [18.3, 37.5, 15.1, 13.7, 2.5, 2.3, 4.8]
election_2024 = [21.96, 18.01, 13.20, 12.40, 7.36, 6.46, 6.33]

poll_colors = ['#ec3442', '#fcb21f', '#e7d517', '#052b58', '#66acd4', '#330791', '#078140']
election_colors = ['#f3858d', '#fdd078', '#f0e573', '#697f9a', '#a3cde5', '#846abd', '#6ab38c']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Romania Opinion Polls')

plt.savefig('Europe/SouthEurope/Romania Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()