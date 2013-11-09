from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'My New App'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'you@example.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'cee44454-1d4e-42bd-8f54-8bcba4631628'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
