import matplotlib.pyplot as plt
import numpy as np

parties = ['ALP', 'L/NP', 'GRN', 'ONP']
polling_2025 = [36.0, 30.0, 12.0, 9.0]
election_2025 = [34.56, 31.82, 12.20, 6.40]

poll_colors = ['#e03c43', '#1e519a', '#079a3e', '#f67110']
election_colors = ['#f08583', '#7896c2', '#6ac28b', '#f9a96f']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2025, width=width, color=election_colors, label='2025 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Australia Opinion Polls')

plt.savefig('Oceania/Asia-Pacific/Australia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()