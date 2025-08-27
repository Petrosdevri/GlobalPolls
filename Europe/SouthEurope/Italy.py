import matplotlib.pyplot as plt
import numpy as np

parties = ['FdI', 'PD', 'M5S', 'Lega', 'FI', 'Azione', 'IV', 'AVS', '+E', 'NM']
polling_2025 = [28.9, 22.3, 12.8, 8.6, 8.5, 3.1, 2.4, 6.4, 1.8, 1.0]
election_2022 = [25.98, 19.04, 15.43, 8.79, 8.11, 7.78, 7.78, 3.64, 2.83, 0.91]

poll_colors = ['#0d3c69', '#e91e26', '#f5dc51', '#008000', '#0087dc', '#063394', '#cf2f85', '#be3457', '#fbc218' , '#2149a7']
election_colors = ['#6d8aa5', '#f1787c', '#f9ea96', '#66b266', '#66b7ea', '#6984be', '#e282b5', '#d8859a', '#fcda74', '#7991ca']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Italy Opinion Polls')

plt.savefig('Europe/SouthEurope/Italy Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()