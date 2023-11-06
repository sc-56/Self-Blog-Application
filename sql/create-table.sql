CREATE TABLE questions (
    id      serial          primary key,
    title   varchar(255)    unique, 
    date_   varchar(255),
    type_   varchar(255),
    answer  varchar(255)
);