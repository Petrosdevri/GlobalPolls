import matplotlib.pyplot as plt
import numpy as np

parties = ['Likud', 'Together', 'RZ-Zehut', 'OY', 'B&W-IRP', 'Shas', 'UTJ', 'YB', "Ra'am", 'JL', 'Dem', 'Yashar', 'Res.', 'AY']
polling_2026 = [24, 15, 5, 8, 0, 8, 8, 9, 5, 6, 9, 21, 1, 1]
election_2022 = [32, 24, 7, 6, 8, 11, 7, 6, 5, 5, 4, 0.1, 0.1, 0.1]

poll_colors = ['#1c5ca4', '#2a2a78', '#1a274c', '#ec3322', '#04bcf4', '#040404', '#0c2c6c', '#9ac0e2', '#307c34', '#01b2ac', '#243ce4', '#60baf2', '#68692d', '#8e35bf']
election_colors = ['#769dc8', '#6969a0', '#757d93', '#f3847a', '#68d6f8', '#686868', '#6d80a6', '#c2d9ed', '#82b085', '#4dc9c4', '#7b8aee', '#8fcef5', '#95966c', '#af71d2']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='October 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Israel Opinion Polls')

plt.savefig('Asia/MiddleEast/Israel Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()