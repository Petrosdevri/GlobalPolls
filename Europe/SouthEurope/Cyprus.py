import matplotlib.pyplot as plt
import numpy as np

parties = ['DISY', 'AKEL', 'DIKO', 'ELAM', 'EDEK', 'DIPA', 'KOSP', 'ALMA', 'Volt']
polling_2025 = [23.2, 20.5, 8.2, 16.4, 4.1, 1.4, 2.7, 15.1, 2.7]
election_2021 = [27.77, 22.34, 11.29, 6.78, 6.72, 6.10, 4.41, 0.10, 0.10]

poll_colors = ['#1f5088', '#7f221f', '#ff7e00', '#000000', '#164f46', '#06acec', '#0d6839', '#97ac2c', '#512478']
election_colors = ['#7896b7', '#b27a78', '#ffb166', '#666666', '#739590', '#69cdf3', '#6da488', '#c0cd80', '#967bae']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Cyprus Opinion Polls')

plt.savefig('Europe/SouthEurope/Cyprus Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()