import matplotlib.pyplot as plt
import numpy as np

parties = ['KOK', 'PS', 'SDP', 'KESK', 'VAS', 'VIHR', 'SFP', 'KD', 'LIIK']
polling_2025 = [19.0, 11.7, 25.0, 15.7, 10.1, 8.5, 4.0, 3.4, 1.1]
election_2023 = [20.82, 20.06, 19.95, 11.29, 7.06, 7.04, 4.31, 4.22, 2.42]

poll_colors = ['#04345c', '#ecdf62', '#f54b4b', '#3bac2e', '#f00a64', '#016844', '#ffdd93', '#2b66c8', '#b42079']
election_colors = ['#68859d', '#f3eba0', '#f99393', '#89cd81', '#f66ca2', '#66a48e', '#ffeabe', '#7fa3de', '#d279ae']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Finland Opinion Polls')

plt.savefig('Europe/NorthEurope/Finland Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()