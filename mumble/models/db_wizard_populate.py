from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_todo,10)
     populate(db.t_correspondance,10)
     populate(db.t_assignment,10)
