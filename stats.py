import sys

with open(sys.argv[1]) as f:
    if len(sys.argv) < 2: 
        sys.exit("Usage: python3 main.py <path to book>")
#        print("Usage: python3 main.py <path to book>")
    else:
        a = f.read()
        count_this = a.split()
        number = len(count_this)

    decap = a.lower()
    
       
def char_count(decap):
    counts = {}

    for element in decap:
        if element in counts:
            counts[element] += 1

        else:
            counts[element] = 1

    return counts

#def sort_count(counts):
    
    #sorted_counts = sorted(counts)

    dict = {}
    #for key in sorted_counts:
     #   dict[key] = counts[key]

    #return dict

def sort_count(counts: dict):
    return dict(sorted(counts.items(), reverse=True, key=lambda x: x[1]))

