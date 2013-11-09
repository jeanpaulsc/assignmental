def index():
    """ this controller returns a dictionary rendered by the view
        it lists all idea nodes
    >>> index().has_key('nodes')
    True
    """
    nodes = db().select(db.node.id,db.node.title,orderby=db.node.title)
    return dict(nodes=nodes)

@auth.requires_login()
def create():
    """creates a new node thread"""
    form = SQLFORM(db.node).process(next=URL('index'))
    return dict(form=form)

def show():
    """expands node insights and children"""
    this_node = db.node(request.args(0,cast=int)) or redirect(URL('index'))
    db.node_id.default = this_node.id
    form = SQLFORM(db.show).process() if auth.user else None
    nodecomments = db(db.node_id==this_node.id).select()
    return dict(node=this_node, comments=nodecomments, form=form)

@auth.requires_login()
def edit():
    """edit an existing node node"""
    this_node = db.node(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.node, this_node).process(next = URL('show',args=request.args))
    return dict(form=form)

@auth.requires_login()
def documents():
	"""browser, edit all documents attached to a certain node"""
	node = db.node(request.args(0,cast=int)) or redirect(URL('index'))
	db.document.node_id.default = node.id
	db.document.node_id.writable = False
	grid = SQLFORM.grid(db.document.node_id==node.id,args=[node.id]) 
	return dict(node=node, grid=grid)

def user():
    return dict(form=auth())
	
def download():
    """allows downloading of documents"""
    return response.download(request, db)

def search():
    """an ajax thought search node"""
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword', _onkeyup="ajax('callback', ['keyword'], 'target');")), target_div=DIV(_id='target'))
	
def callback():
	"""an ajax callback that returns a <ul> of links to thought nodes"""
	query = db.node.title.contains(request.vars.keyword)
	nodes = db(query).select(orderby=db.node.title)
	links = [A(p.title, _href=URL('show',args=p.id)) for p in nodes]
	return UL(*links)
	
def news():
    """generates rss feed form the node nodes"""
    response.generic_patterns = ['.rss']
    nodes = db().select(db.node.ALL, orderby=db.node.title)
    return dict(
    	title = 'node rss feed',
	    link = 'http://127.0.0.1:8000/thinker/default/index', description = 'idea news',
	    created_on = request.now,
	    items = [
	        dict(title = row.title,
	            link = URL('show', args=row.id),
	            description = MARKMIN(row.body).xml(),
	            created_on = row.created_on
	            ) for row in nodes])

service = Service()

@service.xmlrpc
def find_by(keyword):
    """finds nodes that contain keyword for XML-RPC"""
    return db(db.node.title.contains(keyword)).select().as_list()
				
def call():
    """exposes all registered services, including XML-RPC"""
    return service()