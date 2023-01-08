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