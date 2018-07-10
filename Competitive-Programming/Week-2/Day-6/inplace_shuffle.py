import random

def get_random(floor,ceiling):
    return random.randint(floor, ceiling)
    
def shuffle(the_list):

    # Shuffle the input in place
    n = len(the_list)
    for i in range(0,n-1):
        j = get_random(i,n-1)
        the_list[i],the_list[j] = the_list[j],the_list[i]


sample_list = [1, 2, 3, 4, 5]
print ('Sample list:', sample_list)

print ('Shuffling sample list...')
shuffle(sample_list)
print (sample_list)