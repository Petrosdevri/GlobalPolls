import matplotlib.pyplot as plt
import numpy as np

parties = ['FPÖ', 'ÖVP', 'SPÖ', 'NEOS', 'Grüne', 'KPÖ']
polling_2025 = [37.0, 19.0, 20.0, 9.0, 10.0, 4.0]
election_2024 = [28.85, 26.27, 21.14, 9.14, 8.24, 2.39]

poll_colors = ['#055ca6', '#51dcee', '#e22713', '#c81666', '#74a208', '#7f0000']
election_colors = ['#699dc9', '#96eaf4', '#ed7d71', '#de73a3', '#abc76a', '#b26666']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Austria Opinion Polls')

plt.savefig('Europe/WestEurope/Austria Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()