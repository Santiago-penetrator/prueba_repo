from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], #permite los origenes
        allow_methods=["*"], #permite los metodos
        allow_headers=["*"], #permite los headers
        
    )