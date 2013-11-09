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
def todo_manage():
    form = SQLFORM.smartgrid(db.t_todo,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def assignment_manage():
    form = SQLFORM.smartgrid(db.t_assignment,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def correspondance_manage():
    form = SQLFORM.smartgrid(db.t_correspondance,onupdate=auth.archive)
    return locals()

