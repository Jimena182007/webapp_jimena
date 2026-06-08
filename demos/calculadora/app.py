import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'

)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()
    
class Calculadora:
    def GET(self):
        return render.calculadora()

if __name__ == "__main__":
    app.run()