import os

folder_path = "waka_ama_res/WakaNats2017"

for filename in os.listdir(folder_path):

        # Only extract finals files
        if "Final" not in filename:
                print("There is no final in", filename)
                continue
        else:
                file_path = os.path.join(folder_path, filename)

                with open(file_path, 'r', encoding='latin-1') as file:
                        # Read all the contents of the file
                        contents = file.read()
                        print(contents)
