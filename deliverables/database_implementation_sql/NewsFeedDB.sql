CREATE DATABASE IF NOT EXISTS news_feed_db;

USE news_feed_db;

CREATE TABLE IF NOT EXISTS users (
    user_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    password VARCHAR(40) NOT NULL,
    e_mail VARCHAR(35) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE IF NOT EXISTS  posts(
    post_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    content VARCHAR(255),
    last_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(post_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS  comments(
    comment_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    content VARCHAR(255),
	last_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(comment_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS  likes(
    like_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    PRIMARY KEY(like_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS  shares(
    share_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    content VARCHAR(255),
    PRIMARY KEY(share_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(post_id) REFERENCES posts(post_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS  relationship_type(
    relationship_type_id INT NOT NULL AUTO_INCREMENT,
    type varchar(25) NOT NULL,
    PRIMARY KEY(relationship_type_id)
);

CREATE TABLE IF NOT EXISTS  relationship_status(
    relationship_status_id INT NOT NULL AUTO_INCREMENT,
    status varchar(25) NOT NULL,
    PRIMARY KEY(relationship_status_id)
);

CREATE TABLE IF NOT EXISTS  followers_friends(
    from_user_id INT NOT NULL,
    to_user_id INT NOT NULL,
    relationship_type_id INT NOT NULL,
    relationship_status_id INT NOT NULL,
    PRIMARY KEY(from_user_id, to_user_id),
    FOREIGN KEY(relationship_type_id) REFERENCES relationship_type(relationship_type_id) ON DELETE CASCADE,
    FOREIGN KEY(relationship_status_id) REFERENCES relationship_status(relationship_status_id) ON DELETE CASCADE
);
