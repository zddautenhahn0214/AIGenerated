9/12/23
*I had to use something called jupyter to run the program how i wanted, instructions that I used to instal and run it are listed at the bottom where other '*' is.
It also uses the dependecies
pandas
matplotlib
ipywidgets

pip install pandas matplotlib ipywidgets


For this project I wanted to visualize how household spending catagories have or have not changed over the years. For example what percentage of a households expenses was on housing? This was mainly prompted by increasing complaints and issues with rent prices compared to income that people are experinceing in various places in the country.
At the same time I wanted to test more of the limits of Code Interpreter and chatGPT's ability to read uploaded files. So I got the household expenses data from the Buerue of Statistics and formated it into a csv file, uplaoded that files to chatGPT and asked it to visualize the data for me using pie charts for each year.

Here is the prompt for that:
"
I have compiled all the data into this new csv file, i now like to write a program to visualize this data by having a slider bar along a line to select a year, then for each year display a pie chart containing
Food (Source 1)	Housing (Source 1)	Apparel & Services (Source 1)	Transportation (Source 1)	Healthcare (Source 1)	Entertainment (Source 1)	Personal Insurance & Pensions (Source 1)	Other (Source Math)
to display a breakdown of average spending percentages and how those ratios have or have not changed over the last 2 decades.

Answer: Let's work this out in a step by step way to be sure we have the right answer
"

This code worked after a little back and forth debugging as usual and the code was a good visualization of the data for what I was interested in.




*I had to use something called jupyter to run the program how i wanted.
Here is what the ai had to say on how to use it:


Zach:
the pie chart looks right but I dont see the slider or anyway to change what year is being displayed




ChatGPT
I'm sorry for the oversight. If you are running the code in a Jupyter Notebook or Jupyter Lab environment, the slider should be displayed. However, if you are running it in a different environment, the interactive widget might not display.

To ensure the slider works in a Jupyter environment, you also need to enable the ipywidgets extension. Here's how to do it:

Install the widgetsnbextension:
Copy code
pip install widgetsnbextension
Enable the extension:
bash
Copy code
jupyter nbextension enable --py widgetsnbextension
If you're using Jupyter Lab, you will also need to install the @jupyter-widgets/jupyterlab-manager labextension:

bash
Copy code
jupyter labextension install @jupyter-widgets/jupyterlab-manager
After setting up the above, restart your Jupyter Notebook or Jupyter Lab and then run the code I provided. You should see both the pie chart and the interactive slider.




User
im running on a windows 10 machine in powershell




ChatGPT
Thank you for clarifying.

Running interactive visualizations directly in a PowerShell terminal won't work as you've experienced. However, Jupyter Notebook is a versatile tool that supports such interactive visualizations and is commonly used for data analysis and visualization tasks.

Here's how you can set it up:

Install Jupyter Notebook: If you don't have Jupyter installed, you can install it using pip:
Copy code
pip install jupyter
Launch Jupyter Notebook: In your PowerShell terminal, navigate to the directory where you want to create or have your notebook and run:
Copy code
jupyter notebook
This will open a web browser with Jupyter's dashboard.

Create a New Notebook: In the Jupyter dashboard, click on the "New" button (usually in the top right) and select a Python environment. This will create a new Jupyter notebook.

Paste the Code: Once you're in the notebook, you can paste the code I provided into a cell and run the cell. The interactive visualization with the slider should display correctly.

Enable ipywidgets (if not done): As mentioned previously, ensure ipywidgets is enabled. Since you're on Windows and using PowerShell, the commands I previously mentioned should work directly in your terminal.

By following the above steps, you'll be able to see and interact with the pie chart using the slider to select different years.




