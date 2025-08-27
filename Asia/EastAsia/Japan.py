import matplotlib.pyplot as plt
import numpy as np

parties = ['LDP', 'CDP', 'DPFP', 'Komei', 'Ishin', 'Reiwa', 'JCP', 'Sansei', 'CPJ', 'SDP', 'Mirai']
polling_2025 = [23.1, 8.7, 8.3, 3.8, 3.7, 3.3, 2.8, 8.2, 1.8, 0.7, 1.9]
election_2024 = [26.73, 21.20, 11.32, 10.93, 9.36, 6.98, 6.16, 3.43, 2.10, 1.73, 0.10]

poll_colors = ['#3da128', '#074092', '#f6ba0f', '#f05d84', '#b5d343', '#e2057e', '#e3242c', '#ec6520', '#1e86d5', '#06a8e9', '#5bd1c3']
election_colors = ['#8ac67e', '#6a8cbd', '#f9d56f', '#f69db5', '#d2e48e', '#ed69b1', '#ee7b80', '#f3a279', '#78b6e5', '#69caf1', '#9ce3db']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Japan Opinion Polls')

plt.savefig('Asia/EastAsia/Japan Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()