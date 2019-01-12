import os
import time
from selenium import webdriver
import urllib.request

# Loads the driver.
driver = webdriver.Chrome()


# Class used to get through artstation's block of spider header
# (or any other site's block, for that matter).
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def links():
    links_to_images = driver.find_elements_by_class_name("project-image")
    # Initiates list
    links_list = []

    # Get all links to liked collections/artwork.
    for link in links_to_images:
        links_list.append(link.get_attribute('href'))
    return links_list


def ensure_amount_of_likes_correct():
    # Initiates the list of links to likes.
    links_list = links()
    # Gets the amount of likes.
    input("enter when done with scrolling")
    
    links_list = links()
    print(len(links_list))
    return links_list    


def get_username():
    # Requests user to put in their artstation username to get their likes.
    response = input("Please enter your artstation username: ")

    if response == "":
        print("No input, quitting")
        driver.quit()
        quit()

    return response


# Opens the webpage for likes.
opener = AppURLopener()
driver.get("https://www.artstation.com/" + get_username() + "/likes")
print("Opened webpage")

links_list = ensure_amount_of_likes_correct()

# Looks through the link_list for items.

for link in links_list:
    driver.get(link)

    # Finds the elements with the class artwork-image.
    images = driver.find_elements_by_xpath(
        "//div[@class=\"artwork-image\"]/img")

    for image in images:
        src = image.get_attribute("src")
        # Strips the query on the right of the filename.
        filename = src.rstrip("1234567890?")
        # If else statement needed to get the filename,
        # the path length is different depending on if it is a .gif file or not.
        if filename.endswith(".gif"):
            filename = filename[72:]
        else:
            filename = filename[69:]

        # Downloads the image to the folder which in the script is being run.
        opener.retrieve(src, filename)

print("Done downloading all the files")

quit()
# Quits the currently loaded driver, to ensure that no instance is left after finishing the script.
driver.quit()
