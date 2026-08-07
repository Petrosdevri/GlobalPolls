import matplotlib.pyplot as plt
import numpy as np

parties = ['Abdul El-Sayed', 'Mike Rogers']
polling_2026 = [42.3, 46.7]
election_2026 = [0.10, 0.10]

poll_colors = ['#0444cc', '#d31e2a']
election_colors = ['#4f7cdb', '#e06169']

x = np.arange(len(parties))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(x + width/10, election_2026, width=width, color=election_colors, label='2026 Election')
ax.bar(x - width/10, polling_2026, width=width, color=poll_colors, label='August 2026 Polling')

ax.set_ylabel('%')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_title('Michigan US Senate Opinion Polls')

plt.savefig('America/UnitedStates/Michigan US Senate Opinion Polls.png', dpi=300, bbox_inches='tight')
plt.show()