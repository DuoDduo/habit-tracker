from a2wsgi import WSGIMiddleware
from run import app

# Wrap the existing WSGI app (Flask) to be accessible to ASGI servers (like Uvicorn)
asgi_app = WSGIMiddleware(app)
