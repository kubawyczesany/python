from flask import Flask, request

def create_app ():
    app = Flask(__name__)

    @app.route('/convert/<value>', defaults={
        'in_unit': 'C', 'out_unit': 'F'
    })
    @app.route('/convert/<in_unit>/<float:value>/<out_unit>')
    @app.route('/convert/<in_unit>/<int:value>/<out_unit>')

    def convert (in_unit, value, out_unit):
        cases = {
            ('C','F'): (9/5, 32),
            ('F','C'): (5/9, -32*5/9)
        }
        a, b = cases.get((in_unit, out_unit), (1, float('nan')))

        in_value = float(value)
        out_value = a * in_value + b
        if request.args.get('verbose') == 'true' :
            return f'''
                <p><strong>{in_value}</strong> {in_unit}
                is equal to 
                <strong>{out_value}</strong> {out_unit}
                </p>
            '''   #this is f_string, which is displayed as a html in browser
        return str(out_value)

    return app

create_app().run('0.0.0.0')
