# Графы
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Таблица затрат
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Родители
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    # Пройти через каждый узел
    for node in costs:
        cost = costs[node]

        # Если это самая низкая стоимость и до сих пор и еще не была обработана ...
        if cost < lowest_cost and node not in processed:
            # установить его как новый самый дешевый узел.
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

# Найти самый дешевый узел, который вы еще не обработали.
node = find_lowest_cost_node(costs)

# Если вы обработали все узлы, то этот цикл while завершен.
while node is not None:
    cost = costs[node]

    # Пройдите через всех соседей этого узла
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]

        # Если дешевле добраться до этого соседа, пройдя через этот узел ...
        if costs[n] > new_cost:
            # обновить стоимость для этого узла
            costs[n] = new_cost
            # Этот узел становится новым родителем для этого соседа.
            parents[n] = node
    
    # Отметить узел как обработанный.
    processed.append(node)
    # Найти следующий узел для обработки и выполните цикл.
    node = find_lowest_cost_node(costs)


print('Стоимость от начала до каждого узла:')
print(costs)