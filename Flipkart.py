import requests
from bs4 import BeautifulSoup
import openpyxl

# Load the HTML content from the local file (flipkart.html)
with open('flipkart.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class "_1xHGtK _373qXS"
product_divs = soup.find_all('div', class_='_1xHGtK _373qXS')

# Open an Excel file for writing
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers to the Excel sheet
sheet['A1'] = 'Product Name'
sheet['B1'] = 'Product Price'

# Loop through each div and extract product name and price
for index, product_div in enumerate(product_divs, start=2):
    # Try to find the product name with class "IRpwTa"
    product_name_element = product_div.find('a', class_='IRpwTa')
    product_name = product_name_element.text.strip() if product_name_element else ''

    # Try to find the product price with class "_30jeq3"
    product_price_element = product_div.find('div', class_='_30jeq3')
    product_price = product_price_element.text.strip() if product_price_element else ''

    # Write the data to the Excel sheet
    sheet[f'A{index}'] = product_name
    sheet[f'B{index}'] = product_price

# Save the Excel file
workbook.save('output.xlsx')

print('Data written to output.xlsx')
# nadeem
