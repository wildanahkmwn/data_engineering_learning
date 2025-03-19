CREATE TABLE IF NOT EXISTS crypto_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10),
    price NUMERIC,
    timestamp TIMESTAMP
);