from bs4 import BeautifulSoup

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Get Section id's from MainPage
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
with open("tst.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    doc = soup.prettify()

# old script from https://www.skytowner.com/explore/extracting_attribute_values_in_beautiful_soup
# for el in soup.find_all("section"):
#     if el.has_attr("id"):
#         print(el.attrs["id"])

# modified to store values for later retrieval
# https://stackoverflow.com/questions/39366134/how-to-store-values-retrieved-from-a-loop-in-different-variables-in-python

damnit = []
for el in soup.find_all("section"):
    if el.has_attr("id"): 
        damnit.append(el.attrs["id"])
print(damnit)
    # print not actually part of the functionality, for testing purposes only
    # only returns the id of the first section in a list when implemented as a function?

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Get new or updated section from external page, clean html, insert
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
with open("txt.html") as jp:
    soupy = BeautifulSoup(jp, 'html.parser')
    dok = soupy.prettify()
    # switch = ['doctype', 'html', 'head', 'title', 'meta', 'style', 'body', 'font', 'span']
    # for x in switch: 
    # using switch variable to flip through the list on 3 lines of code to do the same function as
    # this all typed out?

# Keep this for proof of concept (section: a regular expression)
# https://www.geeksforgeeks.org/get-a-list-of-all-the-heading-tags-using-beautifulsoup/
# beautifulsoup get list of tags

# switch = ['doctype', 'html', 'head', 'title', 'meta', 'style', 'body', 'font', 'span']
# hekkit = []
# for tags in soupy.find_all(switch):
#     hekkit.append(tags.name)
# print(hekkit)

# strip excess tags, add new tags to switchList as needed to maintain clean up input to MainPage
switch = ['doctype', 'html', 'head', 'title', 'meta', 'style', 'body', 'font', 'span']
hekkit = []
for tags in soupy.find_all(switch):
    tags.decompose()
    hekkit.append(tags.decomposed)
print(hekkit)

# strip all attributes
# for tags in soupy.find_all():
#     del tags.attrs[]
#     hekkit.append(tags.decomposed)
# print(hekkit)
# dang_ol
# dangnabbit
# yemayne