import web
import math 

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
        numero_1 = 0.0
        numero_2 = 0.0
        resultado = 0.0
        return render.calculadora(numero_1, numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        operacion = formulario.get('operacion')
        
        if operacion == "limpiar":
            return render.calculadora(0.0, 0.0, 0.0)
            
        numero_1 = float(formulario['numero_1'])
        numero_2 = float(formulario['numero_2'])
        resultado = 0.0

        if operacion == "sumar":
            resultado = numero_1 + numero_2           
        elif operacion == "restar":
            resultado = numero_1 - numero_2     
        elif operacion == "multiplicar":
            resultado = numero_1 * numero_2           
        elif operacion == "dividir":
            resultado = numero_1 / numero_2           
        elif operacion == "potencia":
            resultado = numero_1 ** numero_2            
        elif operacion == "raiz":
            resultado = numero_1 ** 0.5             
        elif operacion == "modulo":
            resultado = numero_1 % numero_2

        return render.calculadora(numero_1, numero_2, resultado)
    
if __name__ == "__main__":
    app.run()