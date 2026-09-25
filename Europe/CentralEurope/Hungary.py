import matplotlib.pyplot as plt
import numpy as np

parties = ['TISZA', 'Fidesz-KDNP', 'MH', 'DK', 'MKKP']
polling_2025 = [68.0, 22.0, 7.0, 1.0, 1.0]
election_2022 = [55.26, 36.72, 5.72, 1.08, 0.65]

poll_colors = ['#ea4654', '#f17425', '#6a8b1e', '#0f6bb1', '#d7d5d5']
election_colors = ['#f29098', '#f6ab7c', '#a5b978', '#6fa6d0', '#e7e5e5']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Hungary Opinion Polls')

plt.savefig('Europe/CentralEurope/Hungary Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()