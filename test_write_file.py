from functions.write_file import write_file

print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result1)

print("\n" + "="*60 + "\n")

print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result2)

print("\n" + "="*60 + "\n")

print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result3)
