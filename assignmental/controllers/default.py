# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def todo_item_manage():
    form = SQLFORM.smartgrid(db.t_todo_item,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def assignments_manage():
    form = SQLFORM.smartgrid(db.t_assignments,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def todo_log_manage():
    form = SQLFORM.smartgrid(db.t_todo_log,onupdate=auth.archive)
    return locals()

