if __name__ == "__main__":
    string = "I am a teacher and I love to inspire and teach people"
    words = set()
    for word in string.split():
        words.add(word)
    print("Number of unique words: " + str(len(words)))
