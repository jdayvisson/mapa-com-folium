from flask import Flask, request, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', estado=request.args.get('estado', default='SP', type=str))

@app.route('/map')
def map():
    estado_selecionado = request.args.get('estado', default='SP', type=str)
    brasil_map = folium.Map(location=[-14.235, -51.925], zoom_start=4)

    estados = {
        "SP": [-23.550520, -46.633308],
        "RJ": [-22.906388, -43.172222],
    }

    for estado, coordenadas in estados.items():
        if estado == estado_selecionado:
            folium.Marker(coordenadas, popup=f"{estado}", icon=folium.Icon(color='red')).add_to(brasil_map)
        else:
            folium.Marker(coordenadas, popup=f"{estado}", icon=folium.Icon(color='blue')).add_to(brasil_map)

    mapa_html = brasil_map._repr_html_()
    return render_template('index.html', estado=estado_selecionado, mapa=mapa_html)

if __name__ == '__main__':
    app.run(debug=True)
