# ComicSearch
A tool to search every comic books characters appearances.
This tool searches through comics to find the appearances of characters. It breaks the appearances into 4 categories, featured, supporting, villains and other. This enables the user to choose exactly how they want to read characters. It is also able to search for when 2 or more characters appear in a comic together

#### Making the Project
This is the full report on this project and how I made it

The foundations of this project are from one of the Applied Learning Tasks (ALT) for Leaving Cert Computer Science, specifically ALT2 analytics. I used code I had made for this ALT and the skills I had learned as a starting point for this project. You can see the full report of the project [here](https://sites.google.com/a/lccgmail.com/backupsite/project-reports/alt2-project?authuser=1)

For this project I used information from marvel.fandom.com . This search tool is only for Marvel comics as I am more familiar with Marvel comics and would be able to recognise an error easier.

To start this project I web scrapped the links of every marvel comic. I then used those links to web scrape the characters that appear in each comic. I initial used code from my ALT2 project but found it inefficient when applied to a larger data set so I decided to redo the code. When web scraping the information from each comic site I spent time analysing the HTML. As you can see in the below screenshot there is different categories for how the character appeared. I wanted to keep this and add it into my search tool. It was difficult to get the information from each category due to inconsistencies on the website. To combat this I used test cases. I used a sample of websites, all of which had slightly different layouts or orders to the categories, to make sure I was able to get all the data accurately.

Once I had all my data I cleaned it to get rid of any Null or irrelevant information. I began making the search function. I started by making a character selection area so people can choose the character they want. This is when I started to make the search system. I had some trouble adapting the search to include more than one character. I tried many way to do it and used pseudo-code to help me come up with the working solution 

#### Improvements
I think there are many ways to improve my code and I would like to expand the functionality of this project when I have a chance. 
To improve this project I would like to:
- Add a UI as this currently runs in a python terminal. 
- Improve the search algorithm as I have recently learned about search algorithms and would like to make mine more efficient .
- Change the text outputs as it currently uses the exact links that were originally scrapped which isn’t very user friendly.
- Add additional functionality like sorting by date and adding aliases.
- Update the web scraping code as it no longer works correctly due the the source code of marvel.famdom.com being changed.
