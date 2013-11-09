db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

db.define_table('concept',
    Field('title'),
    Field('relation'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now), 
    Field('created_by', 'reference auth_user', default=auth.user_id), 
    format='%(title)s')

db.define_table('insight',
    Field('concept_id', 'reference_concept') ,   
    Field('generaton', 'integer'),
    Field('subject'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now), 
    Field('created_by', 'reference auth_user', default=auth.user_id))

db.define_table('spawn',
    Field('concept_id', 'reference page'),
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

db.concept.title.requires = IS_NOT_IN_DB(db, 'concept.title')
db.concept.body.requires = IS_NOT_EMPTY()
db.concept.created_by.readable = True
db.concept.created_by.writable = False
db.concept.created_on.readable = True
db.concept.created_on.writable = False

db.insight.body.requires = IS_NOT_EMPTY()
db.insight.concept_id.readable = db.insight.concept_id.writable = False
db.insight.created_by.readable = db.insight.created_by.writable = False
db.insight.created_on.readable = db.insight.created_on.writable = False

db.spawn.body.requires = IS_NOT_EMPTY()
db.spawn.concept_id.readable = db.spawn.concept_id.writable = False
db.spawn.created_by.readable = db.spawn.created_by.writable = False
db.spawn.created_on.readable = db.spawn.created_on.writable = False

db.document.name.requires = IS_NOT_IN_DB(db, 'document.name')
db.document.page_id.readable = db.document.page_id.writable = False
db.document.created_by.readable = db.document.created_by.writable = False
db.document.created_on.readable = db.document.created_on.writable = False
