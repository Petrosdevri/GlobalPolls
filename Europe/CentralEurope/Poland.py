import matplotlib.pyplot as plt
import numpy as np

parties = ['ZP', 'KO', 'PL2050', 'PSL', 'Lewica', 'Razem', 'Konfederacja', 'KKP']
polling_2025 = [29.2, 28.9, 3.8, 2.8, 6.4, 4.4, 14.1, 5.5]
election_2023 = [35.39, 30.70, 14.41, 14.41, 8.61, 8.61, 7.17, 7.17]

poll_colors = ['#2a3678', '#ef933b', '#f7c618', '#2dd395', '#ac184a', '#840c54', '#132845', '#c3ac53']
election_colors = ['#7f86ae', '#f5be89', '#fadc74', '#81e4bf', '#cd7492', '#b56d98', '#717e8f', '#dbcd97']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2023, width=width, color=election_colors, label='2023 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Poland Opinion Polls')

plt.savefig('Europe/CentralEurope/Poland Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()