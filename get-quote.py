import random
def main():
  # create var f == open "quotes.text"
  f = open("quotes.txt")
  # var quotes == f with readlines() action 
  quotes = f.readlines()
  # close() the f var for use with readlines
  f.close()
  # var last is length of quotes -1 to compensate for 0 being first, not 1
  last = len(quotes) -1
  # var rnd == imported:random with method randint(from 0 to last:var)
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  # print quotes[rnd] + rnd2, end with no newline
  print(quotes[rnd] + quotes[rnd2], end ="")
# if this is named main, run main()
if __name__== "__main__":
  main()
