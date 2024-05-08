"""Task 1: Code Correction

You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them."""


attendees = input("Enter number of attendees: ")
venue = "large hall" if int(attendees) > 100 else "conference room"
print(venue)


"""Task 2: Venue Selection

Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees."""
system = "projector" if venue == "conference room" else "audio system"
print(system)


"""Task 3: Catering Choices

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers"."""

vegetarian = input("Would You Prefer Vegetarian Food?")
recommendation = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"
print(recommendation)
