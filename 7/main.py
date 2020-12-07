
with open('input', 'r') as f:
    lines = f.readlines()


bags = {}
for line in lines:
    words = line.split()
    color = " ".join(words[0:2]).strip()

    bags[color] = {}
    contains = map(lambda x: x.strip(), " ".join(words[4:]).split(','))

    for element in contains:
        bag = element.split(' ')
        quantity = bag[0]

        if quantity == 'no':
            break
        bags[color][" ".join(bag[1:3]).strip()] = int(quantity)




def bag_contains(bag, color):
    for contents in bags[bag]:
        if contents == color:
            return True
        elif bag_contains(contents, color):
            return True
    return False

def bag_contents(color):
    items = 0
    for contents in bags[color]:
        items += bags[color][contents]
        items += bag_contents(contents) * bags[color][contents]
    return items



count = 0
for bag in bags:
    if bag_contains(bag, 'shiny gold'):
        count += 1

#print(count)

print(bag_contents('shiny gold'))

