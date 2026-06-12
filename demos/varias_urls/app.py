import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
    '/usuarios', 'Usuarios'
)
app = web.application(urls, globals())
 
render = web.template.render('templantes')

class Index:
    def GET(self):
        return render.index()
    
class clientes:
    def GET(self):
        return render.clientes()

class Usuarios:
    def GET(self):
        return render.usuarios()
    

if __name__ == "__main__":
    app.run()