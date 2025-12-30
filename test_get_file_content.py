from functions.get_file_content import get_file_content

# Test lorem.txt truncation
print("Testing lorem.txt truncation:")
result = get_file_content("calculator", "lorem.txt")
print(f"Length: {len(result)} characters")
print(f"Ends with truncation message: {result.endswith(']')}")
print(f"Last 100 chars: ...{result[-100:]}")

print("\n" + "="*60 + "\n")

# Test main.py
print('get_file_content("calculator", "main.py"):')
print(get_file_content("calculator", "main.py"))

print("\n" + "="*60 + "\n")

# Test pkg/calculator.py
print('get_file_content("calculator", "pkg/calculator.py"):')
print(get_file_content("calculator", "pkg/calculator.py"))

print("\n" + "="*60 + "\n")

# Test error: outside working directory
print('get_file_content("calculator", "/bin/cat"):')
print(get_file_content("calculator", "/bin/cat"))

print("\n" + "="*60 + "\n")

# Test error: file doesn't exist
print('get_file_content("calculator", "pkg/does_not_exist.py"):')
print(get_file_content("calculator", "pkg/does_not_exist.py"))
