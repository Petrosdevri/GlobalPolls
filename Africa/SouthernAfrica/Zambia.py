import matplotlib.pyplot as plt
import numpy as np

parties = ['UPND', 'PF', 'CF', 'SP']
polling_2026 = [55.0, 10.0, 2.0, 1.0]
results_2026 = [59.0, 38.7, 0.10, 0.10]

poll_colors = ['#d13438', '#1280c4', '#ff8702', '#b0141a']
results_colors = ['#de7073', '#59a6d5', '#ffab4d', '#c75a5e']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, results_2026, width=width, color=results_colors, label='2026 results')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='August 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Zambia Opinion Polls')

plt.savefig('Africa/SouthernAfrica/Zambia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()