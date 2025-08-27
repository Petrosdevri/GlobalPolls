import matplotlib.pyplot as plt
import numpy as np

parties = ['N-VA', 'VB', 'Vooruit', 'CD&V', 'Open VLD', 'PVDA', 'Groen']
polling_2025 = [26.3, 22.8, 13.4, 14.5, 6.1, 8.9, 7.4]
election_2024 = [25.56, 21.81, 13.02, 12.81, 8.75, 8.16, 7.46]

poll_colors = ['#fcbb27', '#fee600', '#f62c07', '#fa6206', '#119ddd', '#7f0000', '#0a867c']
election_colors = ['#fdd67d', '#fef066', '#f9806a', '#fca069', '#70c4ea', '#b26666', '#6cb6b0']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Flanders Opinion Polls')

plt.savefig('Europe/WestEurope/Flanders Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()