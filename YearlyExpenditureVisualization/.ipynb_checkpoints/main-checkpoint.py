import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Load the data
expenditures_data = pd.read_csv("AverageExpendituresOverTime(USA).csv")

# Convert monetary values to numerical format
monetary_columns = expenditures_data.columns[1:]
for col in monetary_columns:
    expenditures_data[col] = expenditures_data[col].replace('[\$,]', '', regex=True).astype(float)

# Calculate spending percentages
expenditure_columns = expenditures_data.columns[4:]
for col in expenditure_columns:
    expenditures_data[col + " (%)"] = (expenditures_data[col] / expenditures_data["Total Average Expenses (Source 1)"]) * 100
expenditures_data_percentage = expenditures_data.iloc[:, -8:]
expenditures_data_percentage.insert(0, "Year", expenditures_data["Year"])

# Function to plot the pie chart for the selected year
def plot_pie_chart(year):
    # Extracting data for the selected year
    selected_data = expenditures_data_percentage[expenditures_data_percentage["Year"] == year].iloc[:, 1:]
    labels = selected_data.columns
    sizes = selected_data.values[0]
    
    # Plotting the pie chart
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f"Average Spending Percentages for {year}")
    plt.show()

# Widget to select the year
year_slider = widgets.IntSlider(
    value=2006,
    min=2000,
    max=2023,
    step=1,
    description='Year:',
    continuous_update=False
)

# Displaying the slider and the pie chart
widgets.interactive(plot_pie_chart, year=year_slider)
