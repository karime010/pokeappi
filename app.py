from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests

app = Flask(__name__)
app.secret_key = "tu_clave"
API = "https://pokeapi.co/api/v2/pokemon/"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST']) 
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name','').strip().lower()
    
    if not pokemon_name:
        flash('por favor ingresa un nombre','error')
        return redirect(url_for('index'))
    
    try:
        resp = request.get(f"{API}{pokemon_name}")
        if resp.status_code == 200:
            pokemon_data = resp.json()
            pokemon_info= {
    'name' : pokemon_data['name'].title(),
    'id' : pokemon_data['id'],
    'height' : pokemon_data['height'] /10,
    'weight' : pokemon_data['weight'] /10,
    'image' : pokemon_data['sprites']['front_default'],
    'types' : [t['type']['name'].title() for t in pokemon_data['types']],
    'abilities' : [a['ability']['name'].title() for a in pokemon_data['abilities']],
    'stats' : {}
}
            return render_template('pokemon.html', pokemon=pokemon_info)
        else:
            flash(f'pokemon "{pokemon_name}"no encontrado', 'error')
            return redirect(url_for('index'))
    except requests.exception.RequestException as e:
        flash('Error al buscar el pokemon','error')
        return redirect(url_for('index'))

@app.route('/pokemon')
def pokemon():
    return render_template("pokemon.html")

if __name__=='__main__':
    app.run(debug=True)