marks = {
    "sai venkat" : 100,
    "shubham" : 78,
    "roshan" : 34
}
print(marks["sai venkat"])

#properties
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.

print(marks["roshan"])
print(marks.keys())
print(marks.values())

marks.update({"sai venkat": 99})
print(marks)


print(marks.get("sai venkat"))  #prints None
print(marks["sai venkat"])      #returns ERROR

