import random

def tally(v):
  # Create a dictionary to store the vote counts for each candidate
  vote_counts = {}

  # Iterate through the votes and count the number of votes for each candidate
  for vote in v:
    if vote in vote_counts:
      vote_counts[vote] += 1
    else:
      vote_counts[vote] = 1

  # Get the names of the candidates in alphabetical order
  candidates = sorted(vote_counts.keys())

  # Print the vote counts for each candidate
  for candidate in candidates:
    print("{}: {}".format(candidate, vote_counts[candidate]))

  # Find the candidate with the most votes
  max_votes = max(vote_counts.values())
  winners = []
  for candidate in candidates:
    if vote_counts[candidate] == max_votes:
      winners.append(candidate)

  # If there is a tie, choose a winner at random
  if len(winners) > 1:
    winner = random.choice(winners)
  else:
    winner = winners[0]

  print("Winner: {}".format(winner))
