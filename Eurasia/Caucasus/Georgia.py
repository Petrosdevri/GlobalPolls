import matplotlib.pyplot as plt
import numpy as np

parties = ['GD', 'CfC', 'UNM', 'SG', 'FG', 'Girchi', 'APG']
polling_2025 = [56.2, 9.5, 7.5, 10.7, 10.0, 3.2, 1.8]
election_2024 = [53.93, 11.03, 10.17, 8.81, 7.78, 3.00, 2.44]

poll_colors = ['#365894', '#0e5a2f', '#d1342b', '#faad15', '#4b2c74', '#04a34b', '#d7a127']
election_colors = ['#869abe', '#6e9c82', '#e3857f', '#fccd72', '#9380ab', '#68c793', '#e7c67d']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2024, width=width, color=election_colors, label='2024 Election')
ax.bar(x - width/10, polling_2025, width=width, color=poll_colors, label='August 2025 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Georgia Opinion Polls')

plt.savefig('Eurasia/Caucasus/Georgia Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()