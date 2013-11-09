def index():
    """ this controller returns a dictionary rendered by the view
        it lists all idea concepts
    >>> index().has_key('concepts')
    True
    """
    concepts = db().select(db.concept.id,db.concept.title,orderby=db.concept.title)
    return dict(concepts=concepts)

@auth.requires_login()
def create():
    """creates a new concept thread"""
    form = SQLFORM(db.concept).process(next=URL('index'))
    return dict(form=form)

def show():
    """expands concept insights and children"""
    this_concept = db.concept(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.concept).process() if auth.user else None
    return dict(form=form)

@auth.requires_login()
def edit():
    """edit an existing concept node"""
    this_concept = db.concept(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.concept, this_concept).process(next = URL('show',args=request.args))
    return dict(form=form)

@auth.requires_login()
def documents():
	"""browser, edit all documents attached to a certain concept"""
	concept = db.concept(request.args(0,cast=int)) or redirect(URL('index'))
	return dict(concept=concept)

def user():
    return dict(form=auth())
	
def download():
    """allows downloading of documents"""
    return response.download(request, db)

def search():
    """an ajax thought search concept"""
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword', _onkeyup="ajax('callback', ['keyword'], 'target');")), target_div=DIV(_id='target'))
	
def callback():
	"""an ajax callback that returns a <ul> of links to thought concepts"""
	query = db.concept.title.contains(request.vars.keyword)
	concepts = db(query).select(orderby=db.concept.title)
	links = [A(p.title, _href=URL('show',args=p.id)) for p in concepts]
	return UL(*links)
	
def news():
    """generates rss feed form the concept concepts"""
    response.generic_patterns = ['.rss']
    concepts = db().select(db.concept.ALL, orderby=db.concept.title)
    return dict(
    	title = 'concept rss feed',
	    link = 'http://127.0.0.1:8000/thinker/default/index', description = 'idea news',
	    created_on = request.now,
	    items = [
	        dict(title = row.title,
	            link = URL('show', args=row.id),
	            description = MARKMIN(row.body).xml(),
	            created_on = row.created_on
	            ) for row in concepts])

service = Service()

@service.xmlrpc
def find_by(keyword):
    """finds concepts that contain keyword for XML-RPC"""
    return db(db.concept.title.contains(keyword)).select().as_list()
				
def call():
    """exposes all registered services, including XML-RPC"""
    return service()