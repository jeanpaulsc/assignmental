# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()

db.define_table('node',
    Field('parent_id', 'reference node'), #default=self.node.id),
    Field('root_id', 'reference node'), #default=node.root), 
    Field('type'),
    Field('title'),
    Field('body'),
    Field('rank', 'reference node'), #default=node.rank+1),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')


