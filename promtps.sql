-- Natural Joins: joining the same named collumns
SELECT foo 
FROM a
JOIN b;

-- NATURAL JOIN ""ON""" 

-- basic way to create a fk, might have problems
bar_id integer REFERENCES bar(bar_id);

-- cascade is how you prevent fails when deleting a foreign key
web_user_id integer REFERENCES web_user(web_user_id) ON DELETE CASCADE;

-- fk constraints your table, it must have a matching entry iAn other table to make uo

--adding a fk after table creation, 

ALTER TABLE child_table
ADD CONSTRAINT constraint_name
FOREIGN KEY (c1) REFERENCES parent_table(p1); 

FULL OUTER JOIN = LEFT JOIN + RIGHT JOIN

--- this will NOT work, it gives you a single 
select created_fate .. from products
where min(event_date)

-- using a subquery to get a singlular valiue 
select created_fate ...
from products
where event_date = (select min(event_date) from products)

with year_counts as (
    select date_part('year', event_date) as year, count (*) as c
    from products
    where event_date is not null 
    group by 1
)
select *
from products
where date_part('year', event_date) = (
    select year
    from year_counts
    order by c desc
    limit 1
);
