file_path=input('путь к файлу')

path_parts=file_path.split('\\')

print(f'каждая часть по отдельности{'\n'.join(path_parts)}')