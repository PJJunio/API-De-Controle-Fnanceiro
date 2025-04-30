CREATE TABLE expenses (
    expenses_ids SERIAL PRIMARY KEY,
    names VARCHAR (25) NOT NULL,
    descriptions CHAR(255),
    amounts NUMERIC(10, 2) NOT NULL,
    categories VARCHAR(50) NOT NULL,
    active BOOLEAN DEFAULT FALSE NOT NULL,
    users_ids INTEGER,
    CONSTRAINT fk_user_expense FOREIGN KEY (users_ids) REFERENCES users(users_ids)
);