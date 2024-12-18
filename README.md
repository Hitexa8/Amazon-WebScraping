# **Amazon Web Scraping Project**

This is a simple project designed to scrape data from the Amazon website.

---

## **Project Structure**

### **1. project.py**
- Uses **Selenium** to automate data collection.
- Fetches the `outerHTML` from the Amazon website.
- Stores the scraped HTML files inside a folder named `data`.

### **2. collect.py**
- Utilizes **BeautifulSoup** and **Pandas** for processing.
- Parses the stored HTML files to extract relevant information like product details.
- Outputs the processed data for analysis and visualization.

---

## **Steps to Execute**

### **1. Install the Required Libraries**
Run the following commands to install the necessary libraries:

```bash
pip install selenium
pip install bs4
pip install pandas
