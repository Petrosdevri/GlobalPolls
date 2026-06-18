import matplotlib.pyplot as plt
import numpy as np

parties = ['CC', 'AA', 'PA', 'SA']
polling_2026 = [29.0, 5.9, 4.7, 12.7]
election_2021 = [53.95, 21.11, 3.95, 0.10]

poll_colors = ['#2c2655', '#313962', '#f7a80e', '#d90012']
election_colors = ['#807c99', '#8388a0', '#faca6e', '#e86670']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='June 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Armenia Opinion Polls')

plt.savefig('Eurasia/Caucasus/Armenia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()