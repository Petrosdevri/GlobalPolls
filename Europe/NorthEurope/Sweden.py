import matplotlib.pyplot as plt
import numpy as np

parties = ['S', 'SD', 'M', 'V', 'C', 'KD', 'MP', 'L']
polling_2025 = [33.9, 20.5, 18.3, 7.0, 5.4, 3.5, 6.3, 2.8]
election_2022 = [30.33, 20.54, 19.10, 6.75, 6.71, 5.34, 5.08, 4.61]

poll_colors = ['#ec1e37', '#fedf09', '#99def9', '#b00000', '#1a4335', '#015fa1', '#2b912c', '#006ab3']
election_colors = ['#f37887', '#feeb6b', '#c1ebfb', '#cf6666', '#758e85', '#669fc6', '#7fbd80', '#66a5d1']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Sweden Opinion Polls')

plt.savefig('Europe/NorthEurope/Sweden Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()