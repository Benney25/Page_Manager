# research tree
[use python, and beautiful soup, to extract html information from the html page](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup)

I should absolutely turn this into a python CLI tool. I will probably be using this enough. 

If I can figure out how to run this program and only call specific functions of the tool, that would be pretty sweet.

## commands:
&nbsp;  
### tag attributes: 
&nbsp;  
tag.name

grab all:
tag.section

import all __ to dictionary
tag.section[]

Rabbit-Trail:
https://stackoverflow.com/questions/24962673/beautiful-soup-getting-tag-id

### modifying tag contents
&nbsp;  
&nbsp;  
&nbsp;  

tag.clear()

tag.decompose()

tag.insert() OR tag.append() - determine later - Likely append



[use a dictionary to store the data retrieved from the HTML page](https://www.w3schools.com/python/python_dictionaries.asp)
https://docs.python.org/3/tutorial/datastructures.html
https://www.geeksforgeeks.org/python-dictionary/

python list
https://developers.google.com/edu/python/lists
https://developers.google.com/edu/
https://edu.google.com/workspace-for-education/classroom/
https://edu.google.com/intl/ALL_us/for-educators/resources/

python sys.argv
https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
https://www.knowledgehut.com/blog/programming/self-variabe-python-examples
https://docs.python.org/3/library/sys.html
https://linuxhint.com/python-sys-argv/
https://click.palletsprojects.com/en/8.1.x/


rabbit trail:
Import "bs4" could not be resolved from sourcePylance
**https://stackoverflow.com/questions/71031131/can-not-use-bs4-even-after-installing-bs4-in-python
**https://docs.python.org/3/library/venv.html
***https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm


sidetrack
https://www.dotcms.com/docs/latest/markdown-syntax#:~:text=Blank%20Lines,-Markdown%20automatically%20joins&text=To%20add%20a%20single%20extra,replacing%20the%20periods%20with%20spaces).

# https://www.skytowner.com/explore/extracting_attribute_values_in_beautiful_soup
# documentation: kinds of filters: a function
for x in soup.find_all("section"):
    if x.has_attr("id"):
        print(x.attrs["id"])
# Need to break-down how the actual f- this works,
# In the original script, 'el' is chosen as the variable because it's short for element.
# The variable could have easily been any variable, but 'el' is chosen for readability
# and ease of understanding. 
# 
# searching the tree: kinds of filters: a function: 
# <tag attribute1="" attribute2=""> 
#   <child>
#       contents
#   </child> 
# </tag>

want to pass beautifulsoup results into variable
https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
functions are not variables - the problem with adding the for-loop to a function may be entirely different than what I'm trying to do.
storing a for loop in a variable python
https://stackoverflow.com/questions/39366134/how-to-store-values-retrieved-from-a-loop-in-different-variables-in-python


# old script from https://www.skytowner.com/explore/extracting_attribute_values_in_beautiful_soup
# for el in soup.find_all("section"):
#     if el.has_attr("id"):
#         print(el.attrs["id"])

# modified to store values for later retrieval
# https://stackoverflow.com/questions/39366134/how-to-store-values-retrieved-from-a-loop-in-different-variables-in-python
