book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
print(book["avocado"])

voted = {}

def check_voter(name):
  if voted.get(name): #if exist returns value in on returns None
    print("kick them out")
  else:
    voted[name] = True
    print("Let them vote")


check_voter("tom")
check_voter("mike")
check_voter("tom")
