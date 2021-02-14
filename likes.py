"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement a function `likes :: [String] -> String`, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
```
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", s"Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
```
For more than 4 names, the number in `and 2 others` simply increases.
"""


def likes(names):
    count = len(names)
    if count == 0:
        return f'no one likes this'
    elif count == 1:
        return f'{names[0]} likes this'
    elif count == 2:
        return f'{names[0]} and {names[1]} like this'
    elif count == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {count - 2} others like this'
