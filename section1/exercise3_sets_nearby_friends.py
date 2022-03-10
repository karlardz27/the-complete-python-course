nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
your_friend = input("Enter your friend's name: ")

# Add the name to the empty set
user_friends.add(your_friend)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
user_friends_in_nearby_people = user_friends.intersection(nearby_people)
print(user_friends_in_nearby_people)
