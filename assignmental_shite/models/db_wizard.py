### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_todo_item',
    Field('f_title', type='string',
          label=T('Title')),
    Field('f_body', type='string',
          label=T('Body')),
    Field('f_status', type='string',
          label=T('Status')),
    Field('f_created_by', type='string',
          label=T('Created By')),
    Field('f_assigned_to', type='string',
          label=T('Assigned To')),
    auth.signature,
    format='%(f_title)s',
    migrate=settings.migrate)

db.define_table('t_todo_item_archive',db.t_todo_item,Field('current_record','reference t_todo_item',readable=False,writable=False))

########################################
db.define_table('t_todo_log',
    Field('f_log_datetime', type='string',
          label=T('Log Datetime')),
    Field('f_action', type='string',
          label=T('Action')),
    Field('f_user_id', type='string',
          label=T('User Id')),
    auth.signature,
    format='%(f_log_datetime)s',
    migrate=settings.migrate)

db.define_table('t_todo_log_archive',db.t_todo_log,Field('current_record','reference t_todo_log',readable=False,writable=False))

########################################
db.define_table('t_assignments',
    Field('f_todo_id', type='string',
          label=T('Todo Id')),
    Field('f_creator_id', type='string',
          label=T('Creator Id')),
    Field('f_assignee_id', type='string',
          label=T('Assignee Id')),
    Field('f_date_messaged', type='string',
          label=T('Date Messaged')),
    Field('f_response', type='string',
          label=T('Response')),
    Field('f_status', type='string',
          label=T('Status')),
    auth.signature,
    format='%(f_todo_id)s',
    migrate=settings.migrate)

db.define_table('t_assignments_archive',db.t_assignments,Field('current_record','reference t_assignments',readable=False,writable=False))
