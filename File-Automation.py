import os
import shutil
from tkinter import Tk, filedialog

folder_path = None

# new directories
image_path = None
videos_path = None
pdf_path = None
zip_path = None
codes_path = None
others_path = None


# CHOOSE DIRECTORY
def choose_directory():
    root = Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a directory
    selected_directory = filedialog.askdirectory()

    return selected_directory

# # Example usage
# chosen_directory = choose_directory()

# if chosen_directory:
#     print(f"User selected directory: {chosen_directory}")
#     # Now you can perform your file and folder operations in the chosen_directory
# else:
#     print("User canceled directory selection.")


# images, videos, pdf, zip, codes, others
def create_directories():
     # List of paths to create
    directories_to_create = [image_path, videos_path, pdf_path, zip_path, codes_path, others_path]

    # Create directories
    for directory in directories_to_create:
        try:
            os.mkdir(directory)
            print(f"Directory '{directory}' created successfully.")
        except FileExistsError:
            print(f"Directory '{directory}' already exists.")
        except Exception as e:
            print(f"Error creating directory '{directory}': {e}")

    print("Directories creation process completed.")

# to be checked
# def rename_files(folder_path, old_name, new_name):
#     for filename in os.listdir(folder_path):
#         if old_name in filename:
#             new_filename = filename.replace(old_name, new_name)
#             old_filepath = os.path.join(folder_path, filename)
#             new_filepath = os.path.join(folder_path, new_filename)
#             os.rename(old_filepath, new_filepath)
#             print(f'Renamed: {filename} to {new_filename}')

# images, videos, pdf, zip, codes, others
def move_files():
    for filename in os.listdir(folder_path):
        lowercase_filename = filename.lower()
        source_filepath = os.path.join(folder_path, filename)

        # Skip system files or directories starting with a dot
        if filename.startswith('.') or os.path.isdir(source_filepath):
            continue

        if lowercase_filename.endswith(('.png', '.jpeg', '.jpg')):
            destination_filepath = os.path.join(image_path, filename)
        elif lowercase_filename.endswith(('.mp4', '.mov')):
            destination_filepath = os.path.join(videos_path, filename)
        elif lowercase_filename.endswith('.pdf'):
            destination_filepath = os.path.join(pdf_path, filename)
        elif lowercase_filename.endswith('.zip'):
            destination_filepath = os.path.join(zip_path, filename)
        elif lowercase_filename.endswith(('.c', '.py', '.sql', '.java', '.r', '.kt')):
            destination_filepath = os.path.join(codes_path, filename)
        else:
            destination_filepath = os.path.join(others_path, filename)

        shutil.move(source_filepath, destination_filepath)

def delete_files(file_extension):
    for filename in os.listdir(folder_path):
        if file_extension in filename.lower():
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f'Deleted: {filename}')

def search_files(keyword):
    matching_files = [filename for filename in os.listdir(folder_path) if keyword.lower() in filename.lower()]
    for i, file in enumerate(matching_files, start=1):
        print(f"[{i}] {file}")

# needs to be checked
def copy_files(source_folder, destination_folder, file_extension):
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(file_extension):
            source_filepath = os.path.join(source_folder, filename)
            destination_filepath = os.path.join(destination_folder, filename)
            shutil.copy(source_filepath, destination_filepath)
            print(f'Copied: {filename} to {destination_folder}')

# old_name = 'old'
# new_name = 'new'
# destination_folder = '/path/to/destination'
# file_extension_to_delete = '.txt'

# create_directories()
# rename_files(folder_path, old_name, new_name)
# move_files(folder_path, destination_folder)
# delete_files(folder_path, file_extension_to_delete)

print("File Automation Menu:")
print("[1] Sort files into their respective file types")
print("[2] Move a specific file type into a folder")
print("[3] Delete files based on file name")
print("[4] Search files by criteria")

user_input = input('\nEnter input: ')

if user_input == '1':
    folder_path = choose_directory()

    # new directories
    image_path = os.path.join(folder_path, 'Images')
    videos_path = os.path.join(folder_path, 'Videos')
    pdf_path = os.path.join(folder_path, 'PDFs')
    zip_path = os.path.join(folder_path, 'ZIP')
    codes_path = os.path.join(folder_path, 'Codes')
    others_path = os.path.join(folder_path, 'Others')

    create_directories()
    move_files()
elif user_input == '2':
    pass
elif user_input == '3':
    folder_path = choose_directory()
    user_input = input('Delete a file or files by criteria (not case-sensitive): ')
    delete_files(user_input.lower())
elif user_input == '4':
    folder_path = choose_directory()
    user_input = input('Enter a keywork of the filename: ')
    search_files(user_input)
else:
    print('Invalid input.')
