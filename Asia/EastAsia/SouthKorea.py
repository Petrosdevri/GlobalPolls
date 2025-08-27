import matplotlib.pyplot as plt
import numpy as np

parties = ['PPP', 'DPK', 'RKP', 'RP', 'PP']
polling_2025 = [23.7, 49.9, 3.5, 3.6, 1.1]
election_2024 = [36.67, 26.70, 24.25, 3.62, 0.10]

poll_colors = ['#e30424', '#152481', '#2773b8', '#e96d08', '#d4041c']
election_colors = ['#ee687b', '#727bb3', '#7dabd4', '#f1a76a', '#e56876']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('South Korea Opinion Polls')

plt.savefig('Asia/EastAsia/South Korea Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()