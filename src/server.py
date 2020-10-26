from eve import Eve

print("Starting server...")
settings = {'DOMAIN': {'': {}}}

app = Eve(settings=settings)
app.run()