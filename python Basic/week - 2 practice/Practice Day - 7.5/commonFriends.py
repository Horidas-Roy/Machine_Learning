a_friends = {"Rahim", "Karim", "Sakib", "Jamal"}
b_friends = {"Sakib", "Jamal", "Rafiq", "Nadim"}

mutual_friends = b_friends.intersection(a_friends)
unique_to_A = a_friends.difference(b_friends)
unique_to_B = b_friends.difference(a_friends)
uniqueFriends = a_friends.union(b_friends)


print(mutual_friends)
print(unique_to_A)
print(unique_to_B)
print(f"Total unique friends: {len(uniqueFriends)}")