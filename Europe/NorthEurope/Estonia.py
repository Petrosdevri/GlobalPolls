import matplotlib.pyplot as plt
import numpy as np

parties = ['Ref', 'EKRE', 'Kesk', 'E200', 'SDE', 'Isamaa', 'Parem', 'EER']
polling_2025 = [12.0, 18.2, 17.4, 3.1, 13.7, 26.8, 6.8, 0.6]
election_2023 = [31.24, 16.05, 15.28, 13.33, 9.27, 8.21, 2.30, 0.96]

poll_colors = ['#fbdc04', '#0978b7', '#06a955', '#312a96', '#d70c09', '#0799e0', '#f7670d', '#97c841']
election_colors = ['#fcea68', '#6baed3', '#69cb99', '#837fc0', '#e76d6b', '#6ac1ec', '#faa36d', '#c0de8d']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Estonia Opinion Polls')

plt.savefig('Europe/NorthEurope/Estonia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()