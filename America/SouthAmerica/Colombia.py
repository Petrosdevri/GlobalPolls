import matplotlib.pyplot as plt
import numpy as np

parties = ['de la Espriella', 'Cepeda', 'Valencia', 'Fajardo', 'López', 'Botero']
polling_2026 = [43.7, 40.9, 6.9, 4.3, 1.0, 0.9]
results_2026 = [0.10, 0.10, 0.10, 6.29, 0.10, 0.10]

poll_colors = ['#6ca6d9', '#8a287f', '#54b5e6', '#3f2a7b', '#168740', '#000000']
results_colors = ['#a6c9e8', '#b87eb2', '#98d2f0', '#8b7faf', '#73b78c', '#666666']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, results_2026, width=width, color=results_colors, label='2026 results')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='May 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Colombia Opinion Polls')

plt.savefig('America/SouthAmerica/Colombia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()