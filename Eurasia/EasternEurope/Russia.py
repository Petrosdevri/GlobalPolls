import matplotlib.pyplot as plt
import numpy as np

parties = ['YR', 'KPRF', 'LDPR', 'SRZP', 'NL']
polling_2025 = [37.5, 9.0, 10.6, 3.7, 5.0]
election_2021 = [49.82, 18.93, 7.55, 7.46, 5.32]

poll_colors = ['#2057b4', '#c00c05', '#0973b0', '#f9b80b', '#0fd0c9']
election_colors = ['#799ad2', '#d96d69', '#6babcf', '#fbd46c', '#6fe2de']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Russia Opinion Polls')

plt.savefig('Eurasia/EasternEurope/Russia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()