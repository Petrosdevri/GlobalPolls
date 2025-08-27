import matplotlib.pyplot as plt
import numpy as np

parties = ['A', 'V', 'M', 'F', 'Æ', 'I', 'C', 'Ø', 'B', 'Å', 'O', 'H']
polling_2025 = [21.0, 10.1, 3.0, 13.8, 9.7, 12.2, 7.0, 6.8, 4.8, 2.3, 7.2, 1.4]
election_2022 = [27.50, 13.32, 9.27, 8.30, 8.12, 7.89, 5.51, 5.13, 3.79, 3.33, 2.64, 0.10]

poll_colors = ['#f15149', '#0d2c97', '#842494', '#eb94d1', '#043c84', '#3fb2be', '#0a4839', '#d2094f', '#d2307e', '#06fa06', '#fcd03b', '#2474fb']
election_colors = ['#f69691', '#6d80c0', '#b57bbe', '#f3bee3', '#688ab5', '#8bd0d8', '#6c9188', '#e46b95', '#e482b1', '#69fc69', '#fde289', '#7babfc']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Denmark Opinion Polls')

plt.savefig('Europe/NorthEurope/Denmark Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()