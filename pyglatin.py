print "PygLatin"
print "Welcome to the Pig Latin Translator"

original = raw_input("Enter a word: ")

if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"

pyg = 'ay'
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_world[1:len(new_word)]
