CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    users_ids SERIAL PRIMARY KEY,
    external_id UUID UNIQUE NOT NULL DEFAULT gen_random_uuid(),
    usernames CHAR(25) NOT NULL UNIQUE,
    passwords CHAR(255) NOT NULL,
    attempts INT DEFAULT 0,
    account_locked BOOLEAN DEFAULT FALSE
);