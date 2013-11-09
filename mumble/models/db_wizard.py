### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_todo',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_todo_archive',db.t_todo,Field('current_record','reference t_todo',readable=False,writable=False))

########################################
db.define_table('t_correspondance',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_correspondance_archive',db.t_correspondance,Field('current_record','reference t_correspondance',readable=False,writable=False))

########################################
db.define_table('t_assignment',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_assignment_archive',db.t_assignment,Field('current_record','reference t_assignment',readable=False,writable=False))
