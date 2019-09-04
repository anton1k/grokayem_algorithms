from collections import deque 

def person_is_seller(name): # Проверяем подходит ли нам это
    return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []   # Этот массив используетсядля отслеживания уже проверенных людей

    while search_queue:
        person = search_queue.popleft()

        if not person in searched: # Проверяется только в том случаи, если не проверялся ранее
            if person_is_seller(person):
                print('Это тот кто нам нужен', person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Помечается как уже проверенный

    return False

search('you')
