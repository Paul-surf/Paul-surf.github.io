import string

with open("day6-input.txt") as fin:
    data = fin.read()

def unique_questions(group):
    chars = set(group)
    if "\n" in chars:
        return len(chars) - 1

    return len(chars)

groups = data.split("\n\n")
total = 0
for g in groups:
    total += unique_questions(g)

print(total)

#part 2


def all_questions(group):
    people = group.split("\n")
    count = 0
    for char in string.ascii_lowercase:
        presentInAll = True
        for p in people:
            if char not in p:
                presentInAll = False
                break
    
        count += presentInAll

    return count


groups = data.split("\n\n")
total = 0
for g in groups:
    total += all_questions(g)

print(total)