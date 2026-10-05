import matplotlib.pyplot as plt
import numpy as np

parties = ['Lula', 'Bolsonaro', 'Caiado', 'Zema', 'Santos', 'Cury']
polling_2026 = [45.2, 47.0, 2.2, 0.3, 2.2, 2.9]
results_2026 = [0.10, 0.10, 0.10, 0.10, 0.10, 0.10]

poll_colors = ['#e51529', '#004f9f', '#fbba12', '#f3712a', '#fcbe26', '#03a9b3']
results_colors = ['#ec5b69', '#4c83bb', '#fcce59', '#f69b69', '#fcd167', '#4ec2c9']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='October 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Brazil Opinion Polls')

plt.savefig('America/SouthAmerica/Brazil Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()