import os
import shutil
from tkinter import Tk, filedialog

folder_path = None

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


# images, videos, pdf, ppt, docx, zip, codes, not specified
def create_directories():
    # new directories
    image_path = folder_path + '/Images'
    videos_path = folder_path + '/Videos'
    pdf_path = folder_path + '/PDFs'
    zip_path = folder_path + '/ZIP'
    codes_path = folder_path + '/Codes'
    others_path = folder_path + '/Others'

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

# def rename_files(folder_path, old_name, new_name):
#     for filename in os.listdir(folder_path):
#         if old_name in filename:
#             new_filename = filename.replace(old_name, new_name)
#             old_filepath = os.path.join(folder_path, filename)
#             new_filepath = os.path.join(folder_path, new_filename)
#             os.rename(old_filepath, new_filepath)
#             print(f'Renamed: {filename} to {new_filename}')

# images, videos, pdf, ppt, docx, zip, codes, not specified
def move_files():
    # new directories
    image_path = folder_path + '/Images'
    videos_path = folder_path + '/Videos'
    pdf_path = folder_path + '/PDFs'
    zip_path = folder_path + '/ZIP'
    codes_path = folder_path + '/Codes'
    others_path = folder_path + '/Others'

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

# def delete_files(folder_path, file_extension):
#     for filename in os.listdir(folder_path):
#         if filename.endswith(file_extension):
#             file_path = os.path.join(folder_path, filename)
#             os.remove(file_path)
#             print(f'Deleted: {filename}')


# old_name = 'old'
# new_name = 'new'
# destination_folder = '/path/to/destination'
# file_extension_to_delete = '.txt'

# create_directories()
# rename_files(folder_path, old_name, new_name)
# move_files(folder_path, destination_folder)
# delete_files(folder_path, file_extension_to_delete)

user_input = input('Choose your mode:\n' +
    '[1] Sort files into their respective file types\n' +
    '[2] Move a specific file type into a folder\n' + 
    '[3] Delete files based on file name\n'
    )

if user_input == '1':
    folder_path = choose_directory()
    create_directories()
    move_files()
elif user_input == '2':
    pass
elif user_input == '3':
    pass
else:
    print('Invalid input.')
