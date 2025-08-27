import matplotlib.pyplot as plt
import numpy as np

parties = ['Fidesz-KDNP', 'DK', 'MH', 'MKKP', 'TISZA']
polling_2025 = [43.0, 4.3, 4.7, 3.5, 42.0]
election_2022 = [54.13, 34.44, 5.88, 3.27, 0.10]

poll_colors = ['#f17425', '#0f6bb1', '#6a8b1e', '#d7d5d5', '#ea4654']
election_colors = ['#f6ab7c', '#6fa6d0', '#a5b978', '#e7e5e5', '#f29098']

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