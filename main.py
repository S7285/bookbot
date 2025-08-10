import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import number
text = f"Found {number} total words"
#print(text)

from stats import char_count, decap
count = char_count(decap)
#print(count)

from stats import sort_count
sorted_count = sort_count(count)

#def exit_program():
#    sys.exit("Usage: python3 main.py <path to book>")


print("=========== BOOKBOT ===========")
print("--------- Word count ----------")
print(text)
print("------- Character count -------")
for char in sorted_count:
    if char.isalpha():
        print(f"{char}: {sorted_count[char]}")

print("============ END =============")



#print(sorted_count)
