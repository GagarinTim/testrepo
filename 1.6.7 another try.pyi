# n = int(input()) # DO NOT DELETE OR ALTERNATE THIS CODE!!!!!! 2nd
n = 12
dictionary = {'G' : ['F'], 'A' : [], 'B' : ['A'], 'C' : ['A'], 'D' : ['B', 'C'], 'E' : ['D'], 'F' : ['D'], 'X' : [], 'Y' : ['X', 'A'], 'Z' : ['X'], 'V' : ['Z', 'Y'], 'W' : ['V']}


def inside_check(child, parent):
    """""""""
    Deep check
    """""""""
    if child_OG in dictionary[parent]:
        return "Yes"
    elif child_OG not in dictionary[parent]:
        for nodes in dictionary[parent]:
            if child_OG in dictionary[nodes]:
                return "Yes"
            elif child_OG not in dictionary[nodes]:
                inside_check(child, nodes)

def check(parent, child):
    if parent in dictionary.keys():
        if child in dictionary[parent] or parent == child:
            return 'Yes'
        elif child not in dictionary[parent] and child in dictionary.values():
            global parent_OG
            parent_OG = parent
            global child_OG
            child_OG = child
            return inside_check(child, parent)
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

# n2 = int(input())
n2 = 8

for x in range(0, n2):
    a, b = input().split(' ')
    print(check(a, b))

print(dictionary.items())