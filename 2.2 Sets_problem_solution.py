"""
We are trying to figure out if we are accidentally paying one
of our employees more than once. Given a list of employee ID's
determine if we have included more than one of their ID's
"""
employees1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 123, 5125, 6436, 43, 3, 435, 1]
employees2 = []
employees3 = [1, 2, 3]
employees4 = [1, 4, 61]

def main(array):
    print(len(array) != len(set(array)))
        
# Expect True
main(employees1)

# Expect False
main(employees2)

# Expect False
main(employees3)

# Expect False
main(employees4)
