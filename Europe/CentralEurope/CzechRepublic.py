import matplotlib.pyplot as plt
import numpy as np

parties = ['Spolu', 'ANO', 'STAN', 'Piráti', 'SPD', 'Přísaha', 'Stačilo!', 'AUTO']
polling_2025 = [20.3, 30.5, 12.4, 8.0, 13.1, 2.5, 8.7, 3.6]
election_2021 = [27.79, 27.13, 15.62, 15.62, 12.32, 4.68, 8.27, 0.10]

poll_colors = ['#00ea29', '#262560', '#c71566', '#000000', '#0f75ba', '#0633f4', '#c40707', '#46aeec']
election_colors = ['#66f27e', '#7c7c9f', '#dd72a3', '#666666', '#6facd5', '#6984f8', '#db6a6a', '#90cef3']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2021, width=width, color=election_colors, label='2021 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Czech Republic Opinion Polls')

plt.savefig('Europe/CentralEurope/Czech Republic Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()