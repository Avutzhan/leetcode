from collections import deque

def person_is_seller(name):
  return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []

def search(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = set()
  while search_queue:
    person = search_queue.popleft()
    if person not in searched:
      if person_is_seller(person):
        print(person + " is a mango seller!")
        return True
      else:
        search_queue += graph[person]
        searched.add(person)
  return False

search('you')

