import os

folder_path = "waka_ama_res/WakaNats2018"
files_categorized = []
disqualified_keywords = ['DNS', 'DQ', 'disqualified', 'Disqualified']
regional_association_dictionary = {}
row_length_bracket = 10

for filename in os.listdir(folder_path):
        # Only extract finals files
        if "Final" not in filename:
                print("There is no final in", filename)
                continue
        else:

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

        # scoring system main routine

        # extract the row into a list, split by the comma
        for row in body:
                row_list = row.split(",")

                # remove empty elements
                while '' in row_list:
                        row_list.remove('')

                # ensure row is complete. if not, skips the row and prints an error
                if len(row_list) < row_length_bracket:
                        print(
                            f"[!] ERROR: row elements are insufficient. Expected row length bracket =={row_length_bracket} row: ==> {row_list} <=="
                        )
                        continue

                # get the place and regional association
                place = int(row_list[0])
                regional_association = row_list[4]
                score = 0

                # apply scores depending on the place
                if place == 1:
                        score = 8
                elif place == 2:
                        score = 7
                elif place == 3:
                        score = 6
                elif place == 4:
                        score = 5
                elif place == 5:
                        score = 4
                elif place == 6:
                        score = 3
                elif place == 7:
                        score = 2
                elif place >= 8:
                        score = 1
                else:
                        print("[!] ERROR: Place value is invalid")
                        continue

                # add the row to the regional association dictionary. Adds the existing score if the regional assoc already added
                if regional_association in regional_association_dictionary:
                        regional_association_dictionary[
                            regional_association] += score
                else:
                        regional_association_dictionary[
                            regional_association] = score

# display
# sort through values
sorted_regional_association_dictionary = dict(
    sorted(regional_association_dictionary.items(),
           key=lambda x: x[1],
           reverse=True))
# output the regional assoc with their ranks and pts
for count, item in enumerate(sorted_regional_association_dictionary):
        print(count + 1, item, sorted_regional_association_dictionary[item])
