create table book
	(ISBN_number		varchar(20),
	 title		varchar(30),
     writer     varchar(15),
	 page_number		numeric(4,0),
     price      numeric(7,0),
     publisher_name      varchar(15),
     theme      varchar(30),
	 primary key (building, room_number)
	);

create table publisher
	(
     publisher_name	varchar(15),
	 publisher_number		varchar(15),
	 publish_date		Date,
	 primary key (building, room_number)
	);

create table theme
	(theme_name		varchar(30),
     relation_theme_name      varchar(30),
	 book_title      varchar(30),
	 primary key (building, room_number)
	);

create table customer
	(cumtomer_ID    varchar(5),
     address		varchar(15),
	 phone__numebr		varchar(15),
     cumtomer_point    numeric(7,0),
     cumtomer_review   varchar(100),
     purchase_book      varchar(30),
	 primary key (building, room_number)
	);

create table writer
	(book_name          varchar(30),
     writer_name		varchar(30),
	 union_writer_name		varchar(30),
	 capacity		numeric(4,0),
	 primary key (building, room_number)
	);
