from pathlib import Path

# Create a Path object for the current directory
current_dir = Path('.')

# Iterate through all files in the directory
for file in current_dir.iterdir():
    if file.is_file():
        print(f"File: {file.name}")

# Create a new directory
new_dir = current_dir / 'new_folder'
new_dir.mkdir(exist_ok=True)

# Create a new file in the new directory
new_file = new_dir / 'new_file.txt'
new_file.write_text('Hello, Everyone!')

# Read the content of the new file
print(new_file.read_text())