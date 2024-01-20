use ai_prasanth;

create table std_info(
Roll_no int not null primary key auto_increment,
Reg_name varchar(50),
sub_name varchar(75),
class_no int ,
reg_id int not null unique,
foreign key (reg_id)  references ai_batch01(S_NO)
);

show tables;

delimiter //
create procedure insert_into_std_info(
in Regnameparam varchar(50),
subnameparam varchar(50),
classnoparam int,
regidparam int )
begin
insert into std_info(Reg_name,sub_name,class_no,reg_id) values(Regnameparam,subnameparam,classnoparam,regidparam);
end//
delimiter ;

call insert_into_std_info('Shanmugapriya','SQL',16,15);
select * from std_info;


