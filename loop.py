import os

folder_path = "waka_ama_res/WakaNats2017"
files_categorized = []
disqualified_keywords = ['DNS', 'DQ', 'disqualified', 'Disqualified']

for filename in os.listdir(folder_path):
        # Only extract finals files
        """if "Final" not in filename:
                print("There is no final in", filename)
                continue
        else:"""

        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='latin-1') as file:
                # Read all the contents of the file
                content = file.read()

                # categorizing into header and body components
                page_category = {'header': '', 'body': []}
                split_content = content.splitlines()
                page_category['header'] = split_content.pop(0)
                page_category['body'] = split_content
                files_categorized.append(page_category)

# open each files
for i in files_categorized:

        # declare the components as a variable
        header = i['header']
        body = i['body']

        # check header if disqualfied
        for word in disqualified_keywords:
                if word in header:
                        print("[!] ERROR: Header Disqualified", header)

        # check body if there is a disqualified row
        for word in disqualified_keywords:
                if word in body:
                        print("[!] ERROR: Body Disqualified", body)

        # check if row in body is disqualified
        for row in body:
                for word in disqualified_keywords:
                        if word in row:
                                print("[!] ERROR: Row Disqualified.", row)
