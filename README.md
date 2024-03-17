**Models Summary:**

**1. Book:**
- Represents a book in the system.
- Attributes:
  - `title`: Title of the book (CharField).
  - `author`: Author of the book (CharField).
  - `quantity`: Total quantity of the book available (PositiveIntegerField).
  - `stock`: Current stock of the book (PositiveIntegerField).
  - `rent_fee`: Fee charged for renting the book (DecimalField).
  - `image`: Image of the book (CloudinaryField).
  - `updated`: Date and time when the book record was last updated (DateTimeField).
  - `created`: Date and time when the book record was created (DateTimeField).
- Methods:
  - `__str__`: Returns the title of the book.

**2. Member:**
- Represents a member/user in the system.
- Attributes:
  - `name`: Name of the member (CharField).
  - `email`: Email address of the member (EmailField).
  - `outstanding_debt`: Amount of outstanding debt owed by the member (DecimalField).
  - `updated`: Date and time when the member record was last updated (DateTimeField).
  - `created`: Date and time when the member record was created (DateTimeField).
- Methods:
  - `__str__`: Returns the name of the member.

**3. Transaction:**
- Represents a transaction of renting a book by a member.
- Attributes:
  - `book`: Foreign key to the Book model, representing the book involved in the transaction (ForeignKey).
  - `member`: Foreign key to the Member model, representing the member involved in the transaction (ForeignKey).
  - `issue_date`: Date when the book was issued to the member (DateField).
  - `return_date`: Date when the book was returned by the member (DateField, nullable).
  - `is_returned`: Indicates whether the book has been returned (BooleanField).
  - `rent_fee_charged`: Fee charged for renting the book in this transaction (DecimalField, nullable).
  - `created`: Date and time when the transaction record was created (DateTimeField).
- Methods:
  - `__str__`: Returns a string representation of the transaction, consisting of the book title and the member name.

**Relationships:**
- Each `Transaction` links a `Book` with a `Member`, representing the action of a member renting a book.
- The `book` and `member` fields in the `Transaction` model establish foreign key relationships with the `Book` and `Member` models, respectively.
- When a `Transaction` is created, it links a specific `Book` with a specific `Member`, and stores the relevant details such as issue date, return date, and rental fee charged.
