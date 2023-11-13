create database MFT;
create table MFT.profile_tbl(Code int primary key auto_increment,
                              name nvarchar(30),
							  family nvarchar(30),
							  id char(30),
                              password varchar(10),
                              status tinyint,
							  email varchar(30));
create table MFT.post_tbl(Code int primary key auto_increment,
                               Postcode int primary key,
                               profilcode int,
                               postrecord char(100),
                               image nvarchar(30),
                               date_time timestamp,
                               foreign key (profilcode) references profile_tbl(code));
create table MFT.comment_tbl(Codes int primary key auto_increment,
                               Postcode int primary key,
                               profilecode int primary key,
                               commentrecord char(100),
                               date_time timestamp);

create table MFT.like_tbl(Codes int primary key auto_increment,
                               Postcode int primary key,
                               profilecode int primary key);


