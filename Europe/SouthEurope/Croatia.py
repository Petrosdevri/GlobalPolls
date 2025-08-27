import matplotlib.pyplot as plt
import numpy as np

parties = ['HDZ', 'SDP', 'DP', 'DOMiNO', 'Možemo', 'Most', 'Centar']
polling_2025 = [29.3, 22.7, 2.1, 1.9, 10.3, 5.8, 1.3]
election_2024 = [34.42, 25.40, 9.56, 9.56, 9.10, 8.02, 0.10]

poll_colors = ['#2b5ca3', '#eb1c24', '#a5a5a5', '#040404', '#c3d446', '#e85726', '#0d7abf']
election_colors = ['#7f9dc7', '#f3767b', '#c9c9c9', '#686868', '#dbe590', '#f19a7c', '#6dafd8']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Croatia Opinion Polls')

plt.savefig('Europe/SouthEurope/Croatia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()