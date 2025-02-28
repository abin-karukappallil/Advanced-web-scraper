[<img src="https://github.com/user-attachments/assets/0ae5661c-f57d-4c9e-aeea-e938edcd815d  " width="70"/>](web.png)


# Advanced Web Scraping User Manual

## Introduction

This web application is designed to help users scrape data from websites using various methods such as scraping by ID, class, element, hidden links, and confidential documents. This manual will guide you through the process of using the application effectively.

## Understanding HTML Attributes: Class, ID, and More

### HTML Attributes

HTML attributes provide additional information about an element. They are written inside the opening tag of an element as `name="value"` pairs.

### Class Attribute

- **Definition**: The `class` attribute is used to assign one or more class names to an HTML element.
- **Key Points**:
    - Multiple elements can share the same class.
    - Class names are case-sensitive.
    - Use a `.` (dot) before the class name in CSS or when selecting it in JavaScript.
- **Example**:

```html
<div class="city">
  <h2>London</h2>
  <p>London is the capital of England.</p>
</div>
```

- **How to Identify Classes for Scraping**:

1. Open the target webpage in your browser.
2. Right-click on the element you want to scrape and select **Inspect**.
3. Look for the `class` attribute in the HTML code.


### ID Attribute

- **Definition**: The `id` attribute uniquely identifies an HTML element within a document.
- **Key Points**:
    - Use a `#` (hash) before the ID name in CSS or when selecting it in JavaScript.
    - IDs are case-sensitive.
- **Example**:

```html
<div id="header">
  <h1>Welcome to My Website</h1>
</div>
```

- **How to Identify IDs for Scraping**:

1. Inspect the webpage using your browser's developer tools.
2. Look for the `id` attribute in the desired element.


### Differences Between Class and ID

| Feature | Class | ID |
| :-- | :-- | :-- |
| **Uniqueness** | Can be shared by multiple elements. | Must be unique within a page. |
| **Selector** | Use `.` (dot) before class name. | Use `#` (hash) before ID name. |
| **Usage** | Ideal for grouping similar elements. | Ideal for targeting specific elements. |

### Other Useful Attributes

1. **Element Selector**: Targets specific HTML tags like `<div>`, `<span>`, etc.
    - Example: `<div>` selects all `<div>` elements on a page.
2. **Hidden Links**: Some links are hidden within a page's source code (e.g., in `<a>` tags without visible text).
    - Example: `<a href="hidden-link.html" style="display:none;">Hidden Link</a>`.
3. **Confidential Documents**: Files like PDFs or Word documents linked on a page.
    - Example: `<a href="confidential.pdf">Download</a>`.

---

## Step-by-Step Guide to Scraping

### 1. Enter the Website URL

- Click on the URL input field and enter the website URL you want to scrape.
- Ensure the URL is correct and complete. (`www.domain.com ❌`),(`https://domain.com ✅`)


### 2. Select the Scraping Method

- Click on the dropdown menu labeled "Select scraping method".
- Choose the appropriate method based on your needs:
    - **Scrape with ID**: Requires an ID selector.
    - **Scrape with Class**: Requires a class selector. You can enable parallel scraping for two classes.
    - **Scrape Element**: Requires an element selector (e.g., `div`, `span`, etc.).
    - **Scrape Hidden Links** or **Scrape Confidential Documents**: Do not require selectors.


### 3. Enter the Selector (If Required)

- If your chosen method requires a selector (ID, class, or element), enter it in the provided input field.
- For parallel scraping with classes, enable the "Parallel scrapping" switch and enter both class selectors.
- Note: Parallel scrapping will only works on the class which has a flow in parallel

### 4. Start Scraping

- Click the "Scrape" button to initiate the scraping process.
- The button will display a loading animation while the data is being scraped.


### 5. View Results

- Once the scraping is complete, the results will be displayed below the form.
- If the result is a downloadable file (e.g., hidden links or documents), a download will be triggered automatically.

---

## Troubleshooting

- **Error Messages**: If an error occurs during scraping, an error message will be displayed. Check your URL and selector for accuracy.
- **Loading Issues**: Ensure your internet connection is stable. If the application hangs, try refreshing the page.

---

## Security Considerations

- Always ensure you have the right to scrape a website. Check the website's `robots.txt` file and terms of service.
- Be respectful of server resources and avoid overwhelming websites with too many requests.

---

By following this guide, you can effectively use the web scraping application to extract data from websites using various methods.


-------------------------------------------------------------




 # Advanced Web Scraper

## Installation 

### Clone Repositories

``` bash 
git clone https://github.com/abin-karukappallil/Advanced-web-scraper
```
### Install Dependencies

``` bash
pip install -r requirements.txt
```

## Usage

``` bash
python main.py
```



![image](https://github.com/user-attachments/assets/63242c07-59be-4a9a-aab1-d70f341e566a)


![image](https://github.com/user-attachments/assets/a0cea67e-0390-44e9-ba66-965b4701a810)

