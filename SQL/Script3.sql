use ai_prasanth;

delimiter $$
drop procedure if exists delete_value; $$
create procedure delete_value(
in tablename varchar(50),
in idname varchar(50),
in id int)
begin
set @statement = concat(' delete from ', tablename , ' where ', idname ,' = ', id);
prepare stmt from @statement;
execute stmt;
end $$
delimiter ; 

call delete_value("ai_batch01","S_NO",30);

call p();
describe ai_batch01;

