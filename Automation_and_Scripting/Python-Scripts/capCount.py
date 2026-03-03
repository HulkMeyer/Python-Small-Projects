import sys

# define Function
def capCount(input_str):
    # Counting the number of capitals
    count = 0;
    # Sum the indices
    idx_sum = 0;
    #create loop to work through given string
    for i in range(len(input_str)):
        if input_str[i].isupper()==True:
            count += 1
            ind = [idx for idx in range(len(input_str)) if input_str[idx].isupper()]
            idx_sum = sum(ind)
    print(count)
    print(idx_sum)

# Take input from command line
input_str = str(sys.argv[1])

capCount(input_str)
