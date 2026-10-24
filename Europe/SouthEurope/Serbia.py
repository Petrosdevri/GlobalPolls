import matplotlib.pyplot as plt
import numpy as np

parties = ['SNS', 'SPS', 'PES', 'SL']
polling_2026 = [44.1, 4.3, 3.0, 37.1]
election_2023 = [48.07, 6.73, 0.10, 0.10]

poll_colors = ['#39395b', '#ee1b23', '#072277', '#a91a32']
election_colors = ['#74748c', '#f35f65', '#51649f', '#c25e6f']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='October 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Serbia Opinion Polls')

plt.savefig('Europe/SouthEurope/Serbia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()