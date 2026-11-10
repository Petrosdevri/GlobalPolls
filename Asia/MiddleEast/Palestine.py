import matplotlib.pyplot as plt
import numpy as np

parties = ['Hamas', 'Fatah', 'Other']
polling_2026 = [37, 41, 23]
election_2006 = [44.45, 41.43, 14.12]

poll_colors = ['#009240', '#f4b838', '#969696']
election_colors = ['#4cb279', '#f7cd73', '#c0c0c0']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2006, width=width, color=election_colors, label='2006 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='August 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Palestine Opinion Polls')

plt.savefig('Asia/MiddleEast/Palestine Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()