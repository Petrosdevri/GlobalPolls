import matplotlib.pyplot as plt
import numpy as np

parties = ['de la Espriella', 'Cepeda']
polling_2026 = [51.22, 44.24]
results_2026 = [43.75, 40.90]

poll_colors = ['#6ca6d9', '#8a287f']
results_colors = ['#a6c9e8', '#b87eb2']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, results_2026, width=width, color=results_colors, label='2026 results')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='May 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Colombia (2nd Round) Opinion Polls')

plt.savefig('America/SouthAmerica/Colombia (2nd Round) Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()