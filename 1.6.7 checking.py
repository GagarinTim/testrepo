n = int(input()) # DO NOT DELETE OR ALTERNATE THIS CODE!!!!!! 2nd
dictionary = {}


def inside_check(graph, start, child):
    cnt = 0
    for nodes in graph[start]:
        if child in graph[start]:
            print('Yes')
            return "Yes"
        elif child not in graph[start] and cnt < len(graph[start]) ^ 2:
            cnt += 1
            inside_check(graph, nodes, child)
        elif child not in graph[start] and cnt > len(edges) ^ 2:
            print('No')
            return 'No'


def check(dictionary, parent, child):
    if parent in dictionary.keys():
        if child in dictionary[parent] or parent is child:
            return 'Yes'
        elif child not in dictionary[parent]:
            global parent_OG
            parent_OG = parent
            global answer
            answer = "No"
            return inside_check(dictionary, parent, child)
    elif parent not in dictionary.keys():
        return "No"


for x in range(0, n):
    a, *b = input().replace(':', ' ').split()  # input will be <parent> <child>
    for x in b:
        if x not in dictionary.keys():
            if x == []:
                dictionary[x] = 'None'
            for x in b:
                dictionary[x] = {a}
        elif x in dictionary.keys():
            for x in b:
                dictionary[x].add(a)

n2 = int(input())

for x in range(0, n2):
    a, b = input().split(' ')
    print(check(dictionary, a, b))

print(dictionary.items())