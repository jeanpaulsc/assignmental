response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Todo Item'),URL('default','todo_item_manage')==URL(),URL('default','todo_item_manage'),[]),
(T('Assignments'),URL('default','assignments_manage')==URL(),URL('default','assignments_manage'),[]),
(T('Todo Log'),URL('default','todo_log_manage')==URL(),URL('default','todo_log_manage'),[]),
]