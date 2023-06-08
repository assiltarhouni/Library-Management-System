# Library Management System

## Description
The Library Management System is a web-based application developed using Flask, HTML, CSS, and XML. It provides a convenient way to manage books and PFE reports in a virtual library. Users can add new books/PFE reports, view the library collection, and perform searches based on titles and authors.

## Features
- User-friendly interface for easy navigation and interaction.
- Add functionality: Users can add new books and PFE reports to the library.
- View functionality: Users can browse and view the collection of books and PFE reports.
- Search functionality: Users can search for books and PFE reports by title or author.
- Data storage: The application stores the library data in an XML file for persistence.

## Installation
1. Clone the repository: `git clone https://github.com/assiltarhouni/library-management-system.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open a web browser and go to `http://localhost:5000` to access the Library Management System.

## Usage
- Home Page: The landing page of the application, providing an overview of the library system.
- Add a book/PFE report: Access the add book/PFE report page to enter details and add new items to the library.
- Library: Browse and view the collection of books and PFE reports.
- Search: Perform a search by entering a title or author to find specific items in the library.

## File Structure
- `app.py`: The main Flask application file containing the routes and logic.
- `templates/`: Directory containing HTML templates for each page.
- `static/`: Directory containing CSS stylesheets and other static files.
- `books.xml`: XML file storing the library data.
- `bibliodtd`: Bibliodtd file for validating the library XML structure.

## Contributing
Contributions to the Library Management System project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
