CREATE TABLE expenses (
    expenses_ids SERIAL PRIMARY KEY,
    names VARCHAR (25) NOT NULL,
    descriptions CHAR(255),
    amounts NUMERIC(10, 2) NOT NULL,
    categories VARCHAR(50) NOT NULL,
    active BOOLEAN DEFAULT FALSE NOT NULL,
    user_external_id UUID REFERENCES users(external_id)
);