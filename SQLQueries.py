GET_USERS = "SELECT users FROM all_users WHERE user_id = '{}'"
CREATE_MAIN_TABLE = "CREATE TABLE all_users(user_id text NOT NULL, users text NOT NULL);"
ADD_USER = "UPDATE all_users SET users = '{}' WHERE user_id = '{}'"
CREATE_USER = "INSERT INTO all_users (user_id, users) VALUES ('{}', ' ')"
GET_ALL_IDS = "SELECT user_id from all_users"