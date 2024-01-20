use ai_prasanth;
call p();
call s();

delimiter ##
create procedure singleupdate(
in tablename varchar (50),
in columnname varchar (50),
in valuechange varchar (50),
in idname varchar (50),
in idparam int )
begin 
set @statement = concat('update ' , tablename, ' set ' , columnname, '=\'',valuechange,'\'', ' where ',idname, '=',idparam);
prepare stmt from @statement;
execute stmt;
end ##
delimiter ;

call singleupdate("system_info","ERROR","working","SNO",3);
call s();