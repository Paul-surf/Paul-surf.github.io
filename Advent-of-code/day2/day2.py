# importere excel ark ind i min python
import csv

# day2 part 1
# åbner min excel fil som data
with open('day2-input.csv') as data:
    reader = csv.reader(data, delimiter=' ')

# aflæser tal, bogstaver og abcde
    vaildCount = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]

        # aflæser tal i 
        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])

        count = 0
        for character in pw:
            if character == letter:
                count += 1
        
        if count >= lower and count <= upper:
            vaildCount += 1

print(vaildCount)

# part 2
# samme fremgangs metode som part1
with open('day2-input.csv') as data:
    reader = csv.reader(data, delimiter=' ')

    vaildCount = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]


        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])

        # her fjerner jeg bogstaver hvis de er på den forkerte plads = invalid
        count = 0
        first = pw[lower-1] == letter
        last = pw[upper-1] == letter

        # Her definere jeg reglen for hvad er vaild, som giver mig et point.
        if (first and not last) or (last and not first):
            vaildCount += 1

print(vaildCount)