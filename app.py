from flask import Flask, render_template, request, redirect
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Define XML file path
xml_file_path = "books.xml"

# Define routes

# Home page
@app.route('/')
def index():
    return render_template("index.html")

# Library page
@app.route('/library')
def library():
    # Read books from XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    books = []
    for book in root.findall("book"):
        book_dict = {
            "title": book.find("title").text,
            "author": book.find("author").text,
            "year": book.find("year").text,
            "type": book.find("type").text if book.find("type") is not None else "",  # Handle missing "type" element
        }
        books.append(book_dict)

    # Read PFE reports from XML file
    for pfe_report in root.findall("pfe_report"):
        pfe_dict = {
            "title": pfe_report.find("title").text,
            "author": pfe_report.find("author").text,
            "year": pfe_report.find("year").text,
            "type": pfe_report.find("type").text if pfe_report.find("type") is not None else "",  # Handle missing "type" element
        }
        books.append(pfe_dict)

    return render_template("library.html", books=books)


@app.route('/add_book', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        book_type = request.form['type']
        if book_type == 'book':
            # Create new book element
            new_book = ET.Element("book")
            new_book_title = ET.SubElement(new_book, "title")
            new_book_author = ET.SubElement(new_book, "author")
            new_book_year = ET.SubElement(new_book, "year")
            new_book_type = ET.SubElement(new_book, "type")

            # Set element values
            new_book_title.text = title
            new_book_author.text = author
            new_book_year.text = year
            new_book_type.text = book_type

            # Add new book element to XML tree
            try:
                tree = ET.parse(xml_file_path)
                root = tree.getroot()
                root.append(new_book)
                tree.write(xml_file_path)
                return redirect('/library')
            except Exception as e:
                print("Error adding book:", str(e))
                return "Error adding book"
        elif book_type == 'pfe_report':
            # Create new pfe element
            new_pfe = ET.Element("pfe_report")
            new_pfe_title = ET.SubElement(new_pfe, "title")
            new_pfe_author = ET.SubElement(new_pfe, "author")
            new_pfe_year = ET.SubElement(new_pfe, "year")
            new_pfe_type = ET.SubElement(new_pfe, "type")

            # Set element values
            new_pfe_title.text = title
            new_pfe_author.text = author
            new_pfe_year.text = year
            new_pfe_type.text = book_type

            # Add new pfe element to XML tree
            try:
                tree = ET.parse(xml_file_path)
                root = tree.getroot()
                root.append(new_pfe)
                tree.write(xml_file_path)
                return redirect('/library')
            except Exception as e:
                print("Error adding pfe:", str(e))
                return "Error adding pfe"
    else:
        return render_template("add_book.html")



@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        search_query = request.form.get('search')
        # Search for books based on the search query
        search_results = []
        tree = ET.parse('books.xml')
        root = tree.getroot()
        for book in root.findall('book'):
            if (search_query.lower() in book.find('title').text.lower() or 
                search_query.lower() in book.find('author').text.lower()):
                book_dict = {}
                book_dict['title'] = book.find('title').text
                book_dict['author'] = book.find('author').text
                book_dict['year'] = book.find('year').text
                book_dict['type'] = book.find('type').text
                search_results.append(book_dict)
        return render_template('search.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
