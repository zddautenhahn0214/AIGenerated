import requests
from bs4 import BeautifulSoup
from lxml import html

# specify the URL of the website to scrape
url = "https://www.seminolestate.edu/computers/competition/samples/2021"

# send a request to the website and get the HTML response
response = requests.get(url)
# html = response.text

# # parse the HTML response using BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # find all elements with the class "prompt" on the page
# prompts = soup.find_all(class_="col-lg-12")



# parse the HTML response using the lxml library
tree = html.fromstring(response.text)


# use an XPath selector to find all elements with the class "prompt" on the page
prompts = tree.xpath('//main//div/div[h3][p][1]//text()')

# for prompt in prompts:
    # print(prompt)
    # print("end prompt")

# open a file for writing
with open("prompts.txt", "w") as f:
    # write the text of each prompt to the file
    for prompt in prompts:
        f.write(prompt + "\n")
        # f.write("end prompt")
        
print('escaped')


# Open the file for reading
with open('prompts.txt', 'r') as f:
    # Create a list to store the blocks of text
    blocks = []
    # Create a variable to store the current block of text
    current_block = []
    # Iterate over the lines in the file
    for line in f:
        # If the line is not empty, add it to the current block
        if line.strip() != '':
            current_block.append(line)
        # If the line is empty and the current block is not empty,
        # add the current block to the list of blocks and reset the
        # current block
        elif current_block:
            blocks.append(current_block)
            current_block = []
    # After reading all the lines in the file, if the current block
    # is not empty, add it to the list of blocks
    if current_block:
        blocks.append(current_block)



# open a file for writing
with open("prompts.txt", "w") as f:
    # At this point, the list of blocks is populated with the blocks of
    # text from the file. You can now iterate over the blocks and process
    # them as needed.
    #number each prompt starting at 1:
    promptNum = 1
    for block in blocks:
        f.write(f"Prompt #{promptNum}: \n")
        f.write("Write some python code to do fulfill the following prompt: \n")
        #increment prompt number
        promptNum = promptNum + 1
        for line in block:
            f.write(line)
        #blank line for spacing
        f.write('\n')


