import matplotlib.pyplot as plt
import numpy as np

parties = ['Likud', 'YA', 'Mafdal-RZ', 'OY', 'B&W-NU', 'Shas', 'Dem', 'UTJ', 'YB', "Ra'am", 'H-T', 'Balad', 'B2026']
polling_2025 = [22, 10, 4, 7, 5, 8, 11, 7, 11, 5, 5, 0.1, 25]
election_2022 = [32, 24, 7, 6, 8, 11, 4, 7, 6, 5, 5, 0.1, 0.1]

poll_colors = ['#1c5ca4', '#043ca4', '#1a274c', '#ec3322', '#04bcf4', '#040404', '#243ce4', '#0c2c6c', '#9ac0e2', '#307c34', '#d42434', '#f4640c', '#19a3bd']
election_colors = ['#769dc8', '#688ac8', '#757d93', '#f3847a', '#68d6f8', '#686868', '#7b8aee', '#6d80a6', '#c2d9ed', '#82b085', '#e57b85', '#f8a26d', '#75c7d7']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Israel Opinion Polls')

plt.savefig('Asia/MiddleEast/Israel Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()