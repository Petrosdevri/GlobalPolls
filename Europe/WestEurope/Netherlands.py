import matplotlib.pyplot as plt
import numpy as np

parties = ['PVV', 'GL-PvdA', 'VVD', 'NSC', 'D66', 'BBB', 'CDA', 'SP', 'Denk', 'PvdD', 'FvD', 'SGP', 'CU', 'Volt', 'JA21']
polling_2025 = [18.6, 16.8, 13.8, 1.1, 7.3, 2.4, 14.9, 4.3, 2.4, 3.3, 2.5, 2.5, 2.6, 1.9, 5.0]
election_2023 = [23.49, 15.75, 15.14, 12.88, 6.29, 4.65, 3.31, 3.15, 2.37, 2.25, 2.23, 2.08, 2.04, 1.71, 0.68]

poll_colors = ['#254471', '#db2128', '#132ebf', '#f0c400', '#04ac43', '#93be1e', '#2cca4c', '#eb1c24', '#05b5b2', '#066a2e', '#a61c16', '#ea5c0d', '#0fa5e3', '#512478', '#252b54']
election_colors = ['#7c8ea9', '#e9797e', '#7181d8', '#f6db66', '#68cd8e', '#bed878', '#80df93', '#f3767b', '#69d2d0', '#69a581', '#c97673', '#f29d6d', '#6fc9ee', '#967bae', '#7c7f98']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Netherlands Opinion Polls')

plt.savefig('Europe/WestEurope/Netherlands Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()