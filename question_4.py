if __name__ == "__main__":
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]
    print("Length of set A: " + str(len(A)))
    it_companies.add("Twitter")
    it_companies.update(['Tencent', 'Vincit'])
    print(it_companies)
    it_companies.remove('IBM')
    print(it_companies)

    # Remove function raises exception if item is not found, but Discard does not
    joined = A.union(B)
    print("Joined: " + str(joined))
    print("A intersection B: " + str(A.intersection(B)))
    print("Is A subset of B: " + str(A.issubset(B)))
    print("Are A and B disjoint: " + str(A.isdisjoint(B)))

    print("A join B" + str(A.union(B)))
    print("B join A" + str(B.union(A)))

    print("Symmetric difference: " + str(A.union(B).difference(A.intersection(B))))

    del A
    del B
    del joined

    age_set = set(age)

    print("Length of Age: " + str(len(age)))

    print("Length of Age Set: " + str(len(age_set)))
