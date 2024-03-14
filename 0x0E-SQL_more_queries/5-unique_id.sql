-- Create the unique_id table if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	NAME VARCHAR(256)
);
