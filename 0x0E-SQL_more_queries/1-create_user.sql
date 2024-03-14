-- Create or update MySQL database hbtn_0d_2
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Create or update MySQL user user_0d_2 and grant SELECT privileg
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges
FLUSH PRIVILEGES;
