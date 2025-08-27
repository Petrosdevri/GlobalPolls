import matplotlib.pyplot as plt
import numpy as np

parties = ['Smer', 'PS', 'Hlas', 'OĽaNO', 'KDH', 'SaS', 'SNS', 'Republika', 'MA', 'Demokrati']
polling_2025 = [18.9, 20.8, 10.7, 7.3, 6.3, 6.8, 3.4, 10.1, 4.0, 4.9]
election_2023 = [22.95, 17.96, 14.70, 8.90, 6.82, 6.32, 5.63, 4.75, 4.39, 2.93]

poll_colors = ['#ce2d2d', '#05bbfa', '#84153b', '#4a5354', '#1d3c6c', '#9ac322', '#2b2b3b', '#ca151c', '#f48b24' , '#4c168b']
election_colors = ['#e18181', '#69d6fc', '#b57289', '#929798', '#778aa6', '#c2db7a', '#7f7f89', '#df7276', '#f8b97b', '#9373b9']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Slovakia Opinion Polls')

plt.savefig('Europe/CentralEurope/Slovakia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()