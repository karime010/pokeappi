from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

API="https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key = "tu_clave_secreta"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search',methods=['POST']) 
def search_pokemon():
    pokemon_name = request.form.get('pokemon_name','').strip().lower()
    
    if not pokemon_name:
        flash('por favor ingresa un nombre','error')
        return redirect(url_for('index'))
    
    resp = requests.get(f"{API}{pokemon_name}")
    
    if resp.status_code == 200:
        pokemon_data =resp.json()
        return render_template('pokemon.html', pokemon=pokemon_)


#Informacion basica 
pokemon_info= {
    'name' : pokemon_data['name'].title(),
    'id' : pokemon_data['id'],
    'height' : pokemon_data
}


if __name__=='__main__':
    app.run(debug=True)