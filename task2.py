"""
Task 2: Film Night Prep
You're helping your community plan a Friday Film Night for kids. The initial list of movie genres to be shown includes:
genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]

1. Add the genre "Drama" at the end of the list because parents requested it.
2. Someone mistakenly added "Fantasy" twice. Make sure there's only one "Fantasy" in the list.
3. The organizer wants to know how many genres are now planned to be shown.
4. Display the second and second-to-last genres to verify diversity.

→ Modify the list and display the required results.
"""

genres = ["Adventure", "Comedy", "Animation", "Fantasy", "Sci-Fi", "Documentary", "Fantasy"]
genres.append("Drama")
print("The new list after adding Drama", genres)
genres.remove(genres[3])
print("The list after removing Fantasy", genres)
print(len(genres))
print("The second genre is", genres[1], "and the second to the last genre is", genres[-2])
print("The new list is now", genres)

