import os
import shutil

def main():
    folder_path = "C:/Users/arwin/OneDrive/Desktop"
    destination_folder = "C:/Users/arwin/OneDrive/Desktop/Desktop"
    files = os.listdir(folder_path)
    file_ignore = {"Discord", "Docker Desktop", "Postman", "Trash", "Proton VPN", "ASRRGBLED", "Battle.net", "Desktop", "clear"}

    for filename in files:
        file_name_without_ext, file_extension = os.path.splitext(filename)
        if file_name_without_ext not in file_ignore:
            try:
                source_file_path = os.path.join(folder_path, filename)
                destination_file_path = os.path.join(destination_folder, filename)
                shutil.move(source_file_path, destination_file_path)
                print(f"File '{filename}' moved to '{destination_folder}'.")
            except:
                print(f"Error occurred while moving file '{filename}'.")

if __name__ == "__main__":
    main()
