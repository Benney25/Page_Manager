# why do I have element here again? element module is not accessed
import bs4 as bs4
from bs4 import BeautifulSoup, element, Doctype


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Get Section id's from MainPage
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# print('fileAddress of mainPage:')
# mainPage = input()
with open("tst.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    doc = soup.prettify()


def findSections():
    seclist = []
    for el in soup.find_all("section"):
        if el.has_attr("id"): 
            seclist.append(el.attrs["id"])
    return(seclist)

print('All section id\'s: ' + str(findSections()))
    # print not actually part of the functionality, for testing purposes only

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Get new or updated section from external page, clean html, insert
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# print('fileAddress of contentImport file:')
# contentImport = input()
with open("txt.html") as jp:
    souq = BeautifulSoup(jp, 'html.parser')
    dok = soup.prettify()


# Check all elements present in document against elements I want to remove, and elements I want to keep
def checkTags():
    listedElements = ['doctype', 'head', 'title',  'meta', 'style', 'script', 'html', 'body', 'font', 'span']
    elementWhiteList = ['p', 'br', 'br/', '\\n']
    unlistedElements = []
    
    # removes doctype
    # https://www.programcreek.com/python/example/127734/bs4.Doctype
    for item in souq.children:
                if isinstance(item, bs4.Doctype):
                    item.extract()
   
    # True filter value matches everything it can and will allow a string match against any item in that list
    for tags in souq.find_all(True):
        y = tags.name
        if y not in listedElements and elementWhiteList:
            unlistedElements.append(y)
        else:
            continue

    print('Listed Elements: ' + str(listedElements))
    print('Unlisted Elements: ' + str(unlistedElements))
checkTags()

# NewRule: Don't try to do multiple tasks with the same function. 
# If you have more than one task per function, give each task its own function.
# Why do I need to use tags.name for checktags() but not for removeTags()?

# Remove tags without losing any actual content.
def removeTags():
    delete = ['doctype', 'head', 'title',  'meta', 'style', 'script']
    remove = ['html', 'body', 'font', 'span']
    for tags in souq.find_all(delete):
        
        tags.decompose() 
    for tags in souq.find_all(remove):
        
        tags.unwrap()
removeTags()




# strip all attributes
# for tags in soupy.find_all():
#     del tags.attrs[]
# print()

# dang_ol
# dangnabbit
# yemayne


# def removeAttributes():
# del soupy['*']
# tag = soupy.a
# del tags['*']
# del atr['*']
# print(tag.get[])

# removeAttributes()





print(souq.prettify())


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Get Section id's from MainPage
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# TechWithTim Beautifulsoup tutorial 2: 10:45mins
# https://youtu.be/lOzyQgv71_4
# Can I over-write the file I had opened to edit?
def savechanges():
    with open("changed.html", "w") as file:
              file.write(str(doc))