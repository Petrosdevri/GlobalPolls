import matplotlib.pyplot as plt
import numpy as np

parties = ['PP', 'PSOE', 'Vox', 'Sumar', 'Podemos', 'ERC', 'Junts', 'EH Bildu', 'EAJ-PNV', 'BNG', 'CC', 'UPN', 'SALF']
polling_2025 = [30.3, 25.5, 17.7, 6.7, 6.4, 1.6, 1.8, 1.4, 1.3, 1.0, 0.5, 0.2, 1.8]
election_2023 = [33.06, 31.68, 12.38, 12.33, 12.33, 1.89, 1.60, 1.36, 1.12, 0.62, 0.47, 0.21, 0.10]

poll_colors = ['#048bd4', '#fa0404', '#5bc137', '#e21655', '#926af2', '#ffb232', '#04c3b3', '#67d7c9', '#0da35e', '#78b3da', '#f5d44f', '#0e57af', '#755e4c']
election_colors = ['#68b9e5', '#fc6868', '#9cd987', '#ed7399', '#bda5f7', '#ffd084', '#68dbd1', '#a3e7de', '#6dc79e', '#aed1e8', '#f9e595', '#6e9acf', '#ac9e93']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Spain Opinion Polls')

plt.savefig('Europe/SouthEurope/Spain Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()