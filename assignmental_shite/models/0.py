from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Assignmental'
settings.subtitle = 'powered by web2py'
settings.author = 'Jean-Paul McCoy'
settings.author_email = 'jeanpaulsc@gmail.com'
settings.keywords = 'todo'
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'e256f16a-fcee-4b17-a98d-e9ab4eea21ac'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
