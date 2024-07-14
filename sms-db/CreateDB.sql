CREATE TABLE sent_sms(
    host text not null,
    username text not null,
    message text not null,
    phone varchar(11),
    timestamp timestamp default current_timestamp
);

CREATE TABLE fail_sms(
    host text not null,
    username text not null,
    message text not null,
    phone varchar(11),
    timestamp timestamp default current_timestamp
);
