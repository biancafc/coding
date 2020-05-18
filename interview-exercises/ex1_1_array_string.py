# 1.1 - Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?
# Hints:
# 44 - Try a hash table.
# 117 - Could a bit vector be useful?
# 132 - Can you solve it in O(N log N) time? What might a solution like
# that look like?

import string

str = "bianca"
frequency = {}
# string.ascii_lowercase will get all letters to compare with the "str" var
# for char in string.ascii_lowercase:
#     count = 0
#     for i in str:
#         if i == char:
#             count = count + 1
#             frequency[i] = count
#     if count > 1:
#         print("'%s' is not unique" % i)
#
# print(frequency)

 # [{20 => 'a'}, {21 => 'b'}, {23 => c}] ...
hash_table = []

def insert(hash_table, key, value):
    hash_key = key % len(string.ascii_lowercase)
    hash_table.insert(hash_key, {hash_key: value})

def search(hash_table, key):
    hash_key = key % len(hash_table)
    return hash_table[hash_key]

# Add all letters to the hash table
for char in string.ascii_lowercase:
    key = ord(char)
    insert(hash_table, key, char)

for char in str:
    key = ord(char)
    value = search(hash_table, key)
    count = 0
    if value.values()[0] == char:
        if frequency.has_key(char):
            frequency[char] = frequency[char] + 1
        else:
            count = count + 1
            frequency[char] = count

print(frequency)
