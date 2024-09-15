from cutecharts.charts import *    
import pandas as pd

# Open the data
data = pd.read_csv("source/general/fulfillment/applications.csv")

# Extract the labels from the data
labels = list(data["Stage"].unique())

# Count the number of data points
data_filtered = list(data.groupby("Stage").count()["Position"])

# Generate the pie chart usin cutecharts
chart = Pie("Jobs Applied", width="30rem")
chart.set_options(labels=labels)
chart.add_series(data_filtered)

filename = "source/general/fulfillment/applications-pie.html"

# Save the HTML file
chart.render(filename)

# Centre the pie chart

# Path to your HTML file
html_file_path = filename

# Read the existing HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Add <center> tags around the main content of the body
# Here, we assume you want to center everything inside the <body> tag

# Find the position of the opening <body> tag
body_start = html_content.find('<body>') + len('<body>')
body_end = html_content.find('</body>')

# Extract the content inside the <body> tag
body_content = html_content[body_start:body_end]

# Add <center> tags around the body content
updated_body_content = f'<center>{body_content}</center>'

# Reconstruct the full HTML content with centered body
updated_html_content = html_content[:body_start] + updated_body_content + html_content[body_end:]

# Write the updated HTML content back to the file
with open(html_file_path, 'w') as file:
    file.write(updated_html_content)

print(f"Updated HTML file saved at {html_file_path}")
