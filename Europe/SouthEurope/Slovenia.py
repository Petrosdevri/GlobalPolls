import matplotlib.pyplot as plt
import numpy as np

parties = ['GS', 'SDS', 'NSi', 'SD', 'Dem.', 'Levica', 'Res.', 'Prerod', 'PIR', 'SNS']
polling_2026 = [26.0, 28.0, 10.0, 8.0, 4.0, 9.0, 4.0, 3.0, 3.0, 2.0]
election_2026 = [28.66, 27.88, 9.26, 6.71, 6.69, 5.69, 5.49, 3.05, 2.36, 2.24]

poll_colors = ['#0562a2', '#fbdc08', '#64bad3', '#eb1c24', '#0b1259', '#b04946', '#7c5499', '#6e288f', '#000000', '#000000']
election_colors = ['#69a0c7', '#fcea6a', '#a2d5e4', '#f3767b', '#6c709b', '#cf9190', '#b098c1', '#9968b0', '#666666', '#666666']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='September 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Slovenia Opinion Polls')

plt.savefig('Europe/SouthEurope/Slovenia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()