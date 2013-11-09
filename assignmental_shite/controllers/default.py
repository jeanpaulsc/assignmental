# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

@auth.requires_login()
def index():
    
    offers = db(db.t_todo_item.f_assigned_to==auth.user).select()
    return dict(offers=offers)

def error():
    return dict()

    

@auth.requires_login()
def todo_item_manage():
    """
    form = SQLFORM.smartgrid(db.t_todo_item,onupdate=auth.archive)
    return locals()
    """
    query = (db.t_todo_item.f_created_by == auth.user_id)
    form = SQLFORM.grid(query)
 
    return dict(form=form)

@auth.requires_login()
def assignments_manage():
    form = SQLFORM.smartgrid(db.t_assignments,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def todo_log_manage():
    form = SQLFORM.smartgrid(db.t_todo_log,onupdate=auth.archive)
    return locals()
