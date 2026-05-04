DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    ConstituentID TEXT PRIMARY KEY,
    DisplayName TEXT,
    ArtistBio TEXT,
    Nationality TEXT,
    Gender TEXT,
    BeginDate INT,
    EndDate INT,
    Wiki_QID TEXT,
    ULAN TEXT
);

\copy artists FROM 'Artists.csv' WITH (FORMAT csv, HEADER true);

drop table if exists song;

create table song (
    name text,
    duration integer,
    listens integer,
    genre text
);

insert into song (name, duration, listens, genre) values
('Fast As a Shark', 230619, 3990994, 'metal'),
('Restless and Wild', 252051, 4331779, 'metal'),
('Nothing Compares 2U', 375418, 6290521, 'pop'),
('Let''s Get It Up', 233926, 7636561, 'pub rock'),
('Inject The Venom', 210834, 6852860, 'pub rock'),
('Snowballed', 203102, 6599424, 'pub rock'),
('Evil Walks', 263497, 8611245, 'pub rock');

select sum(listens)
from song;

select name, genre, duration
-- subquery here 
from (select name, genre, duration, rank() over (order by duration desc) as rnk 
     from song) ranked
where rnk = 1;

select (ARRAY['deniz', 'kyle', 'derricky'])[3];

with vars as (select 'egg, pizza, burger, rice, banana' 
as term) 
select (string_to_array(term, ', ')) as food_string
from vars; 

select trim('   hi   ');