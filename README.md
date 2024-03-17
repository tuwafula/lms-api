<h1>Summary</h1>
<p>This is a REST API built using django-restframework.
The API is meant for use by libraries for management of library resources.
  </p>
<p>Base models Summary:</p>

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

<p>
  
User Model Summary:
</p>

The `User` model is a custom user model built upon Django's `AbstractUser`, designed to provide enhanced functionality for user management in Django applications.

**Attributes:**
- `first_name`: Represents the first name of the user (CharField).
- `last_name`: Represents the last name of the user (CharField).
- `email`: Represents the email address of the user, and is set as the unique identifier for the user (EmailField).
- `is_staff`: Indicates whether the user has staff permissions (BooleanField).
- `is_superuser`: Indicates whether the user has superuser permissions (BooleanField).
- `avatar`: Represents the avatar (profile picture) of the user, stored as an image file (CloudinaryField).
- `username`: Set to `None` to enforce the use of email as the username.
- `USERNAME_FIELD`: Specifies the field used as the unique identifier for authentication (email).
- `REQUIRED_FIELDS`: Specifies additional fields required when creating a user (none in this case).

**Methods:**
- `create_user(email, password=None, **extra_fields)`: Creates a regular user with the given email and password. Raises a `ValueError` if email or password is not provided.
- `create_superuser(email, password=None, **extra_fields)`: Creates a superuser with the given email and password. Sets `is_staff` and `is_superuser` to `True`. Raises a `ValueError` if `is_staff` or `is_superuser` is not `True`.

**Relationships:**
- Inherits from Django's `AbstractUser`, providing all the standard fields and methods of Django's default user model.
- Utilizes a custom user manager (`CustomUserManager`) to manage user creation and provide additional functionality.

**Avatar Handling:**
- The `avatar` field allows users to upload their profile pictures, which are stored using Cloudinary for efficient handling of image uploads and storage.

**Usage:**
- Designed for use as the primary user model in Django applications, providing a robust foundation for user authentication and management.
- Can be extended or customized further to meet specific application requirements, such as additional user profile information or authentication mechanisms.

**Note:**
- By setting `username` to `None`, the `email` field becomes the unique identifier for authentication purposes, promoting email-based user authentication, which is considered best practice for security and usability reasons.
