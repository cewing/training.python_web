TABLEPRAGMA = "PRAGMA table_info(%s);"


def print_table_metadata(cursor):
    tmpl = "%-10s |"
    rowdata = cursor.description
    results = cursor.fetchall()
    for col in rowdata:
        print tmpl % col[0],
    print '\n' + '-----------+-'*len(rowdata)
    for row in results:
        for value in row:
            print tmpl % value,
        print '\n' + '-----------+-'*len(rowdata)
    print '\n'


def show_table_metadata(cursor, tablename):
    stmt = TABLEPRAGMA % tablename
    cursor.execute(stmt)
    print "Table Metadata for '%s':" % tablename
    print_table_metadata(cursor)


AUTHORS_BOOKS = {
    'China Mieville': ["Perdido Street Station", "The Scar", "King Rat"],
    'Frank Herbert': ["Dune", "Hellstrom's Hive"],
    'J.R.R. Tolkien': ["The Hobbit", "The Silmarillion"],
    'Susan Cooper': ["The Dark is Rising", ["The Greenwitch"]],
    'Madeline L\'Engle': ["A Wrinkle in Time", "A Swiftly Tilting Planet"]
}
