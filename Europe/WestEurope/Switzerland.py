import matplotlib.pyplot as plt
import numpy as np

parties = ['SVP-UDC', 'SP', 'FDP', 'Die Mitte', 'Grüne', 'GLP', 'EVP']
polling_2025 = [29.9, 17.8, 14.3, 14.1, 9.5, 6.6, 2.0]
election_2023 = [27.93, 18.27, 14.25, 14.06, 9.78, 7.55, 1.95]

poll_colors = ['#099f4f', '#e3042c', '#174e97', '#f1940a', '#86b11f', '#b4dc00', '#ecdb17']
election_colors = ['#6bc595', '#ee6880', '#7394c0', '#f6be6c', '#b6d078', '#d2ea66', '#f3e973']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Switzerland Opinion Polls')

plt.savefig('Europe/WestEurope/Switzerland Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()