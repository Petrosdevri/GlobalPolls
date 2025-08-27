import matplotlib.pyplot as plt
import numpy as np

parties = ['AKP', 'CHP', 'MHP', 'İYİ', 'DEM', 'YRP', 'ZP', 'TİP', 'A']
polling_2025 = [31.5, 33.2, 7.9, 5.1, 8.7, 3.1, 4.3, 1.2, 2.0]
election_2023 = [35.62, 25.35, 10.07, 9.69, 8.82, 2.80, 2.23, 1.76, 0.10]

poll_colors = ['#f1ad24', '#e30414', '#b33336', '#4cace4', '#774693', '#474647', '#363635', '#ba141a', '#1b2c4d']
election_colors = ['#f6cd7b', '#ee6872', '#d18486', '#93cdee', '#ad90be', '#909090', '#868685', '#d57275', '#768094']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Turkey Opinion Polls')

plt.savefig('Eurasia/Turkey/Turkey Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()