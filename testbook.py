from book import bookdetails

def test_book_details():
    expected_output = (
        "Book ID: 125\n"
        "Book Title: The Sea\n"
        "Author Name: Ram\n"
        "Year of Publication: 1995"
    )

    actual_output = bookdetails(125, "The Sea", "Ram", 1995)

    assert actual_output == expected_output
