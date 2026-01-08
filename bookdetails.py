def bookdetails(book_id, book_title, author_name, year_of_publication):
    result = (
        f"Book ID: {book_id}\n"
        f"Book Title: {book_title}\n"
        f"Author Name: {author_name}\n"
        f"Year of Publication: {year_of_publication}"
    )
    return result


if __name__ == "__main__":
    book_id = 125
    book_title = "The Sea"
    author_name = "Ram"
    year = 1995

    print(bookdetails(book_id, book_title, author_name, year))
