# -*- coding: utf-8 -*-

db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'actging' or 'smtp.gmail.com:587'
mail.settings.sender = 'jeanpaulsc@gmail.com'
mail.settings.login = ''

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

db.define_table('act',
    Field('kind', 'string', notnull=True),
    Field('title', 'string', notnull=True),
    Field('body', 'text', notnull=True),
    Field('status', 'string', default='new'),
    Field('addressee', 'integer'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format=('%(title)'))

db.act.kind.requires = IS_NOT_EMPTY()
db.act.title.requires = IS_NOT_IN_DB(db, 'act.title')
db.act.body.requires = IS_NOT_EMPTY()
##db.act.addressee.requires = IS_IN_DB(db 'auth.email')
db.act.created_by.readable = db.act.created_by.writable = False
db.act.created_on.readable = db.act.created_on.writable = False

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
