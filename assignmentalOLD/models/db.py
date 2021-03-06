db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# the talented and underpaid members
db.define_table('cybertrooper',
    Field('name', notnull=True),
    Field('email', requires=IS_EMAIL()),
    format='%(name)s')

# the opportunities
db.define_table('projects',
    Field('title', notnull=True),
    Field('description'),
    Field('provider'),
    Field('developer'),
    Field('status', default='open'),
    Field('download'),
    format='%(title)')

db.define_table('logger',
    Field('projects_id'),
    Field('body', 'text',notnull=True),
    Field('posted_on', 'datetime'),
    Field('activity'))
