from datetime import datetime

def add_email():
    if auth.user:
        return auth.user.email
    else:
        return 'None'

db.define_table('todo_item',
    # This table functions for all users
    Field('author', default = get_email()),
    Field('creation_date', 'datetime', default=datetime.utcnow()),
    Field('title', 'text'),
    Field('body', 'text'),
    Field('contact', 'text'),
    Field('status', requires=IS_IN_SET(['accepted', 'denied', 'completed'])),
    format='%(title)s'
    )

db.todo_item.author.writable = False
db.todo_item.id.readable = False
db.todo_item.creation_date.writable = False

"""
db.define_table('assignment',
    Field('todo_item_id'),
    Field('contact'),
    Field('creation_date', 'datetime', default=datetime.utcnow()),
    Field('status', requires=IS_IN_SET(['accepted', 'denied', 'completed'])),

db.assignment.todo_item_id.readable = False
db.assignment.contact.requires = IS_EMAIL()
db.todo_item.creation_date.writable = False
"""