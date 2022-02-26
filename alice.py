
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf_8') as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        print(f"I'm sorry, {filename} was not found.")
    else: 
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {str(num_words)} words.")

for file in filenames:
    filename = "chapter_10/" + file
    count_words(filename)
