from random import randint
from operator import itemgetter
players = list()
player = dict()
ranking = dict()
for cont in range(1, 5):
    player['name'] = 'player' + str(cont)
    player['dice'] = randint(1, 6)
    players.append(player.copy())
ranking = sorted(player, key=itemgetter(1))
print(ranking)