import matplotlib.pyplot as plt
import numpy as np

parties = ['PPLE', 'PTP', 'UTN', 'BJT', 'DP', 'PPRP']
polling_2025 = [46.1, 11.5, 13.2, 9.8, 2.9, 2.7]
election_2023 = [37.99, 28.84, 12.54, 2.99, 2.43, 1.41]

poll_colors = ['#fb6413', '#c61521', '#2e3279', '#625ca8', '#1979ae', '#056539']
election_colors = ['#fca271', '#dc7279', '#8184ae', '#a09dca', '#75aece', '#69a288']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Thailand Opinion Polls')

plt.savefig('Asia/EastAsia/Thailand Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()