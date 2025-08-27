import matplotlib.pyplot as plt
import numpy as np

parties = ['AD', 'PS', 'Chega', 'IL', 'Livre', 'CDU', 'BE', 'PAN']
polling_2025 = [26.3, 23.6, 20.2, 7.3, 9.9, 4.0, 2.8, 3.3]
election_2025 = [31.78, 22.83, 22.76, 5.36, 4.07, 2.91, 1.99, 1.38]

poll_colors = ['#3777af', '#e02229', '#242354', '#07abeb', '#a3c463', '#ea1c25', '#ca0434', '#0a647b']
election_colors = ['#87adcf', '#ec7a7e', '#7b7b98', '#6accf3', '#c7dba1', '#f2767c', '#df6885', '#6ca2af']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2025, width=width, color=election_colors, label='2025 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Portugal Opinion Polls')

plt.savefig('Europe/SouthEurope/Portugal Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()