import streamlit as st

# Set up our app
st.set_page_config(page_title="Personal Library Manager", layout="wide")
st.title("Personal Library Manager")
st.write("Welcome to your personal library manager!")


if "books" not in st.session_state:
    st.session_state["books"] = []


# List of dictionaries to store all books when user adds a book
books_list = []

book_dict = {}





# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.write("Select an option from the sidebar:")
option = st.sidebar.selectbox("Select an option", ["View Books", "Add Book", "Update Book", "Delete Book"])

# View books
if option == "View Books":
    st.subheader("View Books")

    #  loop through st.session_state["books"] and display them.
    for book in st.session_state["books"]:
        st.write(f"**Title:** {book['title']}, **Author:** {book['author']}, **Year:** {book['year']}, genre: {book['genre']}")
    


# Add book
if option == "Add Book":
    st.subheader("Add Book")
    # Here you would typically add a new book to a database or file
    book_dict["title"] = st.text_input("Title of the book:")
    book_dict["author"] = st.text_input("Name of the author:")
    book_dict["year"] = st.number_input("Year of publication:", min_value=1000, max_value=3000, step=1)
    book_dict["genre"] = st.text_input("Genre of the book:")
    book_dict["read_status"] = st.selectbox("Have you read this book?", options=["Read", "Not Read", "Reading"])

    if st.button("Add Book"):
        new_book = {
            "title": book_dict["title"],
            "author": book_dict["author"],
            "year": book_dict["year"],
            "genre": book_dict["genre"],
            "read_status": book_dict["read_status"]
        }
        st.session_state["books"].append(new_book)
        st.success(f"Book '{book_dict['title']}' by {book_dict['author']} added successfully!")
        


# Update book
if option == "Update Book":
    st.subheader("Update Book")
    # Here you would typically fetch and display books from a database or file
    title = st.text_input("Title to update")
    new_author = st.text_input("New Author")
    new_year = st.number_input("New Year", min_value=1000, max_value=3000)
    if st.button("Update Book"):
        # Here you would typically update the book in a database or file
        for book in st.session_state["books"]:
            if book["title"] == title:
                book["author"] = new_author
                book["year"] = new_year
                st.success(f"Book '{title}' updated successfully!")
                break
        else:
            st.warning(f"Book '{title}' not found!")
        st.success(f"Book '{title}' updated successfully!")

# Delete book
if option == "Delete Book":
    st.subheader("Delete Book")
    # Here you would typically fetch and display books from a database or file
    title = st.text_input("Title to delete")
    if st.button("Delete Book"):
        # Here you would typically delete the book from a database or file
        for book in st.session_state["books"]:
            if book["title"] == title:
                st.session_state["books"].remove(book)
                st.success(f"Book '{title}' deleted successfully!")
                break
            else:
                st.success("Book nor found!")

# Footer
st.sidebar.write("© 2023 PS. Personal Library Manager. All rights reserved.")
