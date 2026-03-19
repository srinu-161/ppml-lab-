#loop over set of elements tupple ,list, dict, set
list_1 = [1, 2, 3, 4, 5, 6]
set_1 = {2, 4, 6, 7, 8}
dict_1 = {1: "a", 2: "b", 3: "c"}
tupple_1 = (8, 9, 0, 7)

print("Looping over list:")
for item in list_1:
    print(item)
print("\nLooping over set:")
for item in set_1:
    print(item)
print("\nLooping over dictionary:")
for key, value in dict_1.items():
    print(f"Key: {key}, Value: {value}")

print("\nLooping over tuple:")
for item in tupple_1:
    print(item)