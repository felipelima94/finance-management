create table company(
	id uuid DEFAULT uuid_generate_v4() PRIMARY key,
	fantasy_name varchar(180),
	administrator varchar(200),
	code varchar(6) not null,
	cnpj varchar(30),
	created timestamp not null default current_timestamp,
	updated timestamp not null default current_timestamp
);

create table stock(
	id uuid DEFAULT uuid_generate_v4() PRIMARY key,
	company_id uuid not null,
	stock_type varchar(12) not null,
	operation_type char(1) not null,
	bought_date date not null,
	value numeric(11,4) not null,
	fee numeric(6,4),
	amount numeric(16,8) not null,
	created timestamp not null default current_timestamp,
	updated timestamp not null default current_timestamp,
	foreign key (company_id) references company (id)
);


commit;

select * from pg_stat_activity;

drop table stock;
drop table company;

select exists (select * from company c where c.fantasy_name = 'ExempleB') as anon;
select * from company c;
select * from stock s ;

with purchased as ( 
    select sum(s.value * s.amount) as value, company_id 
    from stock s 
    where s.operation_type != 'V'
    group by s.company_id 
), 
sold as ( 
    select p.value - sum(s.value * s.amount) as avg_price 
    	, p.value as purchased
    	, sum(s.value * s.amount) as sold
    	, s.company_id 
    from stock s
    cross join purchased p 
    where s.operation_type = 'V'
    group by s.company_id, p.value
) 
--select c.code, s.purchased, s.sold, s.avg_price 
select *
from sold s 
right join company c on c.id = s.company_id


with purchased as ( 
    select sum(s.value * s.amount) as value, s.company_id, sum(s.amount) as amount 
    from stock s 
    where s.operation_type != 'V' 
    group by s.company_id 
), 
sold as ( 
    select sum(s.value * s.amount) as value, s.company_id, sum(s.amount) as amount 
    from stock s 
    where s.operation_type = 'V' 
    group by s.company_id 
),
resume as (
	select p.company_id
		, p.amount as amount_purchased
		, 0 as amount_sold
		, p.value as purchased
		, 0 as sold
	from purchased p
	right join company c on c.id = p.company_id 
	union 
	select s.company_id 
		, 0 as amount_purchased
		, s.amount as amount_sold
		, 0 as purchased
		, s.value as sold
	from sold s
	right join company c on c.id = s.company_id 
)
select c.code
	, sum(r.purchased) as total_purchased
	, sum(r.sold) as total_sold
	, sum(r.purchased - r.sold) as total_invested 
	, sum(r.amount_purchased - r.amount_sold) as amount
	, sum(r.purchased - r.sold) / sum(r.amount_purchased - r.amount_sold) as avg_price
from resume r
join company c on c.id = r.company_id
group by c.code



--select sum(s.value * s.amount), s.operation_type, s.company_id 
select s.*
from stock s 
--group by operation_type, company_id 

ALTER TABLE public.stock ADD amount int4 NOT NULL;
ALTER TABLE public.stock ALTER COLUMN amount_ TYPE numeric;
ALTER TABLE public.stock ALTER COLUMN amount_ TYPE numeric(16,8) USING amount_::numeric;




