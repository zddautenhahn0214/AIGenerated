9/18/2023 -updating to upload to github

on 4/6/2023 Used chatGPT4 to try making me generic website templates that I could later cusomize.
Here was the prompt I gave it:
"
write a generic website template. The template should include:
*modern(as of 2020) coding standards for websites
*a nav bar with 4 pages
*a table to put data into
*a basic way to visualize that data
*yellow somewhere in the color scheme
"

Then I asked it to try the same but using React instead.
Had to ask it to debug a little, but it did tell me to create the react app first rather than just give me the code.

The websites mostly work, but need a little tinkering to make links work, which I would do anyways when customizing so I left it. Also they don't look that amazing.



4/6/2023
I wanted a templated website I could use for various different ideas, so asked gpt4 do create it for me using React. 
my reqs were as followed:
"
write a generic website template. The template should include:
*modern(as of 2020) coding standards for websites
*a nav bar with 4 pages
*a table to put data into
*a basic way to visualize that data
*yellow somewhere in the color scheme
"
then clarification for attempt 2:
"
with a more module data table and visualizer, otherwise use the same requirement and write the template using Reactjs
"


First it told me to use the following bash commands:
npx create-react-app my-app
cd my-app

then:
"Now, replace the content of src/App.js with the following code:"
which I did.

after that it said:
"Now, replace the content of src/App.css with the following code:"

there was an error, but it was because I had hit the character limit and needed to continue.

finnally it gave me this messaged to end:
"
Now you have a React app with a modular data table and data visualizer. The `DataTable` and `DataVisualizer` components receive data from the parent component `App`, which makes them reusable and easy to update with new data.
"