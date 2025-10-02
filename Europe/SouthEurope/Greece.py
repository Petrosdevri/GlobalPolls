import matplotlib.pyplot as plt
import numpy as np

parties = ['ND', 'SYRIZA', 'PASOK', 'KKE', 'SP', 'EL', 'NIKI', 'PE', 'MERA25', 'FL', 'NA', 'KD']
polling_2025 = [25.9, 4.5, 14.8, 7.8, 0.1, 10.1, 2.1, 10.0, 5.0, 5.2, 1.4, 5.3]
election_2023 = [40.56, 17.83, 11.84, 7.69, 4.68, 4.44, 3.70, 3.17, 2.50, 0.43, 0.10, 0.10]

poll_colors = ['#1d6ec8', '#d8989d', '#0b753f', '#db1318', '#e6b465', '#4c9cc4', '#bc5a34', '#a53e86', '#eb4326', '#2890de', '#c53638', '#522197']
election_colors = ['#77a8de', '#e7c1c4', '#6cac8b', '#e97174', '#f0d2a2', '#93c3db', '#d69c85', '#c98bb6', '#f38e7c', '#7ebceb', '#dc8687', '#9779c0']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Greece Opinion Polls')

plt.savefig('Europe/SouthEurope/Greece Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()