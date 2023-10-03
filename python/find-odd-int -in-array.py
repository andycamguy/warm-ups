def find_it(seq):
   # Initialize a dictionary to store integer counts
    count_dict = {}
    
    # Iterate through the array and populate the dictionary
    for num in seq:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Iterate through the dictionary to find the odd occurrence
    for num, count in count_dict.items():
        if count % 2 == 1:
            return num

# got the solution from chatgpt.
# what did i learn?

# dictionaries are something I need to learn. brand new territory for me. had no idea how to do it
