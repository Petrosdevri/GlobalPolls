import matplotlib.pyplot as plt
import numpy as np

parties = ['FF', 'FG', 'SF', 'SD', 'Lab', 'Aon', 'II', 'GP', 'PBP-S']
polling_2025 = [20.0, 20.0, 20.0, 8.0, 4.0, 4.0, 5.0, 1.0, 3.0]
election_2024 = [21.86, 20.80, 19.01, 4.81, 4.65, 3.91, 3.55, 3.04, 2.84]

poll_colors = ['#048c3c', '#04bbea', '#0c846c', '#742c8c', '#ec0404', '#44532a', '#04ea54', '#24ac6c', '#dc0c84']
election_colors = ['#68ba8a', '#68d6f2', '#6db5a6', '#ab80ba', '#f36868', '#8e977f', '#68f298', '#7bcda6', '#ea6db5']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Ireland Opinion Polls')

plt.savefig('Europe/NorthEurope/Ireland Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()