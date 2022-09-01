if __name__ == "__main__":
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    n = len(ages)
    sorted(ages)
    print("Sorted: " + str(ages))
    print("Min: " + str(min(ages)))
    print("Max: " + str(max(ages)))
    if n % 2 != 0:
        mid = int(n / 2 - 1)
        median = (ages[mid] + ages[mid + 1]) / 2
        print("Median is: " + str(median))
    else:
        median = ages[int(n / 2)]
        print("Median is: " + str(median))
    print("Average: " + str(sum(ages) / n))
    print("Range: " + str(max(ages) - min(ages)))