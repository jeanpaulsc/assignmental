# coding: utf8

def index():
    """ this controller returns a dictionary rendered by the view
        it lists all wiki acts
    >>> index().has_key('acts')
    True
    """
    received = db.act().select(
        db.act.addressee==auth.user_id,
        db.act.title, 
        orderby=db.act.title)
    sent = db.act().select(
        db.act.created_by==auth.user_id,
        db.act.title).process(next=URL('user/index'))
    return dict(received=received, sent=sent)

@auth.requires_login()
def create():
    """creates a new empty wiki act"""
    form = SQLFORM(db.act).process(next=URL('index'))
    return dict(form=form)

def show():
    """shows a wiki act"""
    this_act = db.act(request.args(0,cast=int)) or redirect(URL('index'))
    db.post.act_id.default = this_act.id
    form = SQLFORM(db.act).process() if auth.user else None
    return dict(page=this_act)

@auth.requires_login()
def edit():
    """edit an existing wiki page"""
    this_page = db.page(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.page, this_page).process(next = URL('show',args=request.args))
    return dict(form=form)

def user():
    return dict(form=auth())
