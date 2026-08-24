import matplotlib.pyplot as plt
import numpy as np

parties = ['Ädilet', 'Auyl', 'Aq Jol', 'Respublica', 'QHP', 'JSDP']
polling_2026 = [71.8, 6.4, 5.1, 5.4, 3.0, 5.2]
election_2023 = [53.90, 10.90, 8.59, 8.41, 6.80, 5.20]

poll_colors = ['#511f98', '#075c49', '#0c4187', '#4875ed', '#dc0f2c', '#0145af']
election_colors = ['#8562b6', '#518c7f', '#547aab', '#7e9ef2', '#e6576b', '#4d7cc7']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='August 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Kazakhstan Opinion Polls')

plt.savefig('Eurasia/CentralAsia/Kazakhstan Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()