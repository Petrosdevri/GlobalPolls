import matplotlib.pyplot as plt
import numpy as np

parties = ['EPP', 'S&D', 'PfE', 'ECR', 'Renew', 'G/EFA', 'The Left', 'ESN', 'NI']
polling_2025 = [22.6, 18.8, 13.2, 10.8, 9.4, 6.8, 10.6, 4.9, 2.9]
election_2024 = [26.1, 18.9, 11.7, 10.8, 10.7, 7.4, 6.4, 3.5, 4.6]

poll_colors = ['#3399ff', '#fb0404', '#2c3262', '#1a64a3', '#ffd700', '#2fa534', '#ba3d3d', '#21527d', '#969696']
election_colors = ['#84c1ff', '#fc6868', '#8084a0', '#75a2c7', '#ffe766', '#82c985', '#d58a8a', '#7997b1', '#c0c0c0']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('European Union Opinion Polls')

plt.savefig('Europe/WestEurope/European Union Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()