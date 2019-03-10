# import ipdb
ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold': 'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

totals_list = {}
for vote in ballots:
    for place, name in vote.items():
        if place == 'gold' and name in totals_list:
            totals_list[name] += 3
        elif place == 'gold' and name not in totals_list:
            totals_list[name] = 3
        elif place == 'silver' and name in totals_list:
            totals_list[name] += 2
        elif place == 'silver' and name not in totals_list:
            totals_list[name] = 2
        elif place == 'bronze' and name in totals_list:
            totals_list[name] += 1
        elif place == 'bronze' and name not in totals_list:
            totals_list[name] = 1

curr_score = 0
for name, points in totals_list.items():
    if points > curr_score:
        curr_winner = name
        curr_score = points

print(totals_list)
print(curr_winner)
