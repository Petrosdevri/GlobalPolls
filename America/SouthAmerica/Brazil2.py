import matplotlib.pyplot as plt
import numpy as np

parties = ['Bolsonaro', 'Lula']
polling_2026 = [48.18, 45.86]
results_2026 = [0.10, 0.10]

poll_colors = ['#004f9f', '#e51529']
results_colors = ['#4c83bb', '#ec5b69']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='October 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Brazil (2nd Round) Opinion Polls')

plt.savefig('America/SouthAmerica/Brazil (2nd Round) Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()