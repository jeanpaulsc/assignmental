from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_todo_item,10)
     populate(db.t_todo_log,10)
     populate(db.t_assignments,10)
