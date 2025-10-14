words = ["sun", "planet", "moon", "star", "universe"]
filter_word = list(filter(lambda word : word if len(word) > 4 else None,words))
print(filter_word)