# print this using for loop
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for num in range(6):
    for i in range(num):
        print(num, end=' ')
    print('')

# see this diagram https://pynative.com/python-for-loop/#h-for-loop-with-range
# then runs a new for-loop on each stage of the first (parent loop). and for each "subloop" print num (parent loop)
# that's how it prints the pattern