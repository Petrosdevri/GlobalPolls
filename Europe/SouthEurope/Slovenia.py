import matplotlib.pyplot as plt
import numpy as np

parties = ['GS', 'SDS', 'NSi', 'SD', 'Levica', 'ZS', 'Res.', 'SNS', 'Vesna', 'Dem.']
polling_2025 = [16.4, 22.7, 4.9, 7.7, 4.3, 2.3, 5.5, 1.8, 1.2, 4.1]
election_2022 = [34.45, 23.48, 6.86, 6.69, 4.46, 3.41, 2.86, 1.49, 1.35, 0.10]

poll_colors = ['#0562a2', '#fbdc08', '#64bad3', '#eb1c24', '#b04946', '#6caa47', '#7c5499', '#000000', '#0aa15f' , '#0b1259']
election_colors = ['#69a0c7', '#fcea6a', '#a2d5e4', '#f3767b', '#cf9190', '#a6cc90', '#b098c1', '#666666', '#6cc69f', '#6c709b']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2022, width=width, color=election_colors, label='2022 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Slovenia Opinion Polls')

plt.savefig('Europe/SouthEurope/Slovenia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()