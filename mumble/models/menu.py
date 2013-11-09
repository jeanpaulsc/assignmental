response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Todo'),URL('default','todo_manage')==URL(),URL('default','todo_manage'),[]),
(T('Assignment'),URL('default','assignment_manage')==URL(),URL('default','assignment_manage'),[]),
(T('Correspondance'),URL('default','correspondance_manage')==URL(),URL('default','correspondance_manage'),[]),
]