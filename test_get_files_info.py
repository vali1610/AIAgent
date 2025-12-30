from functions.get_files_info import get_files_info

print('get_files_info("calculator", "."):\nResult for current directory:')
print(get_files_info("calculator", "."))

print('\nget_files_info("calculator", "pkg"):\nResult for \'pkg\' directory:')
print(get_files_info("calculator", "pkg"))

print('\nget_files_info("calculator", "/bin"):\nResult for \'/bin\' directory:')
print("    " + get_files_info("calculator", "/bin"))

print('\nget_files_info("calculator", "../"):\nResult for \'../\' directory:')
print("    " + get_files_info("calculator", "../"))
