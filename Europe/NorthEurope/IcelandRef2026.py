import matplotlib.pyplot as plt
import numpy as np

parties = ['Yes', 'No']
polling_2026 = [51.7, 48.3]

poll_colors = ['#00bf63', '#ff0000']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, polling_2026, width=width, color=poll_colors, label='August 2026 Referendum')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Iceland Referendum Opinion Polls')

plt.savefig('Europe/NorthEurope/Iceland Referendum Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()