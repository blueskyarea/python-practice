import sys
from math import sqrt
from data import review

def calc_similarity(member1, member2):
  games = set(review[member1].keys())
  distance_list = []

  for game in games:
    distance = pow(review[member1][game] - review[member2][game], 2) 
    distance_list.append(distance)

  print "similarity of " + member1 + " and " + member2
  print 1/(1 + sqrt(sum(distance_list)))

if __name__ == '__main__':
  args = sys.argv
  calc_similarity(args[1], args[2])
