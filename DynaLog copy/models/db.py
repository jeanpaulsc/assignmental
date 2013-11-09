db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

db.define_table('thread',
    Field('title'),
    Field('type'),
    Field('rooted_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')

db.define_table('node',
    Field('parent_id', 'reference_node'),
    Field('title'),
    Field('relation'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now), 
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')

db.define_table('insight',
    Field('node_id', 'reference_node') ,   
    Field('generaton', 'integer'),
    Field('subject'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now), 
    Field('created_by', 'reference auth_user', default=auth.user_id))

db.define_table('spawn',
    Field('node_id', 'reference page'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now), 
    Field('created_by', 'reference auth_user', default=auth.user_id))

db.define_table('document',
    Field('page_id', 'reference page'),
    Field('name'),
    Field('file', 'upload'),
    Field('created_on', 'datetime', default=request.now), 
    Field('created_by', 'reference auth_user', default=auth.user_id), 
    format='%(name)s')

db.node.title.requires = IS_NOT_IN_DB(db, 'node.title')
db.node.body.requires = IS_NOT_EMPTY()
db.node.created_by.readable = True
db.node.created_by.writable = False
db.node.created_on.readable = True
db.node.created_on.writable = False

db.insight.body.requires = IS_NOT_EMPTY()
db.insight.node_id.readable = db.insight.node_id.writable = False
db.insight.created_by.readable = db.insight.created_by.writable = False
db.insight.created_on.readable = db.insight.created_on.writable = False

db.spawn.body.requires = IS_NOT_EMPTY()
db.spawn.node_id.readable = db.spawn.node_id.writable = False
db.spawn.created_by.readable = db.spawn.created_by.writable = False
db.spawn.created_on.readable = db.spawn.created_on.writable = False

db.document.name.requires = IS_NOT_IN_DB(db, 'document.name')
db.document.page_id.readable = db.document.page_id.writable = False
db.document.created_by.readable = db.document.created_by.writable = False
db.document.created_on.readable = db.document.created_on.writable = False
