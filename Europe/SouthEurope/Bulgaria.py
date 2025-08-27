import matplotlib.pyplot as plt
import numpy as np

parties = ['GERB-SDS', 'PP-DB', 'Vazrazdhane', 'DPS-NN', 'BSP-OL', 'APS', 'ITN', 'MECh', 'Velichie']
polling_2025 = [28.3, 15.4, 12.8, 14.6, 9.0, 3.1, 5.2, 7.0, 4.6]
election_2024 = [26.39, 14.21, 13.36, 11.51, 7.57, 7.49, 6.78, 4.60, 4.00]

poll_colors = ['#2269b9', '#0818f0', '#bc9f6b', '#0c62a1', '#d21c25', '#6147aa', '#4fb2d9', '#000000', '#ad3537']
election_colors = ['#7aa5d5', '#6a74f6', '#d6c5a6', '#6da0c6', '#e4767c', '#a090cc', '#95d0e8', '#666666', '#cd8587']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Bulgaria Opinion Polls')

plt.savefig('Europe/SouthEurope/Bulgaria Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()