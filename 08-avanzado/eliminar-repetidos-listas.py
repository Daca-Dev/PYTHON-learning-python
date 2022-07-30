# [1, 1, 2, 2, 3, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_duplicates_sets(some_list):
    without_duplicates = set(some_list)
    return list(without_duplicates)

def run():
    random_list = [1, 1, 2, 2, 3, 4]
    print(remove_duplicates_sets(random_list))

if __name__ == '__main__':
    run()
    
