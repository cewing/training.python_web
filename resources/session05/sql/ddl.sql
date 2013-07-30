-- Schema for a simple book database

-- Author table

CREATE TABLE author(
  authorid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name TEXT
);

CREATE TABLE book(
  bookid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  title TEXT,
  author INTEGER NOT NULL,
  FOREIGN KEY(author) REFERENCES author(authorid)
);
