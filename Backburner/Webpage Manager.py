# # # # # # # # # # # # # # # # # # # # # # # # 
# Importing Files (completed)
# # # # # # # # # # # # # # # # # # # # # # # # 

print('please provide the absolute file address for the main webpage')
mainpage = input()
print('please provide the absolute file address for the new section content')
newcontent = input()

file1 = open(mainpage, 'r')
file2 = open(newcontent, 'r')

page = file1.read()
content = file2.read()

# print(page)
# positive test with: print(content)

# # # # # # # # # # # # # # # # # # # # # # # # 
# Importing the sections from mainpage
# # # # # # # # # # # # # # # # # # # # # # # # 
# search = "<section id=\"" + * + "\">" + * + "</section>"

# def grabsection():

#     for search in file1:
#         if search == "<section id=\"" * "\">" * "</section>":
#             print(search)

# print(grabsection())

# def grabsection():
#     for line in file1:

# def grabsection():
#     open(mainpage, 'r').read().find("<section id=\".+\">.+</section>")
# print(grabsection())

# read by line or read by string?

# page 

# sections = 

# # # # # # # # # # # # # # # # # # # # # # # # 
# Cleaning content from newcontent
# # # # # # # # # # # # # # # # # # # # # # # # 

# content = 
# cleaned = 

# # # # # # # # # # # # # # # # # # # # # # # # 
# Selecting a section
# # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # 
# # If section does not exist :: create it
# # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # 
# # If section exists :: Empty the original section contents
# # # # # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # # # # # # # # # 
# Printing new contents to the section
# # # # # # # # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # # # # # # # 
# Alternative option: filedata = filedata.replace('ram', 'abcd')
# # # # # # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # 
# Cleanup
# # # # # # # # # # # # # # # # # # # # # # # # 

file1.close
file2.close