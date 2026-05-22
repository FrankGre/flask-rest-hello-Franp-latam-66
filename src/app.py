# ==========================================
# ⭐ ENDPOINTS DE FAVORITOS (FAVORITES)
# ==========================================

# 1. Obtener todos los favoritos del usuario actual
@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Simulamos que estamos usando el usuario con ID 1
    current_user_id = 1
    
    # Buscamos en la tabla de favoritos todos los que pertenezcan a este usuario
    user_favorites = Favorite.query.filter_by(user_id=current_user_id).all()
    results = [fav.serialize() for fav in user_favorites]
    
    return jsonify(results), 200

# 2. Añadir un nuevo personaje favorito
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    current_user_id = 1  # Usuario simulado
    
    # Verificamos si ya existe en favoritos para no duplicarlo
    exists = Favorite.query.filter_by(user_id=current_user_id, people_id=people_id).first()
    if exists:
        return jsonify({"msg": "Este personaje ya está en tus favoritos"}), 400
        
    # Si no existe, lo creamos
    new_favorite = Favorite(user_id=current_user_id, people_id=people_id)
    db.session.add(new_favorite)
    db.session.commit()
    
    return jsonify({"msg": "Personaje agregado a favoritos con éxito"}), 200

# 3. Añadir un nuevo planeta favorito
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    current_user_id = 1  # Usuario simulado
    
    # Verificamos si ya existe
    exists = Favorite.query.filter_by(user_id=current_user_id, planet_id=planet_id).first()
    if exists:
        return jsonify({"msg": "Este planeta ya está en tus favoritos"}), 400
        
    new_favorite = Favorite(user_id=current_user_id, planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()
    
    return jsonify({"msg": "Planeta agregado a favoritos con éxito"}), 200

# 4. Eliminar un personaje favorito
@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    current_user_id = 1  # Usuario simulado
    
    # Buscamos el registro exacto que tenga ese usuario y ese personaje
    favorite = Favorite.query.filter_by(user_id=current_user_id, people_id=people_id).first()
    
    if favorite is None:
        return jsonify({"msg": "El personaje no está en tus favoritos"}), 404
        
    db.session.delete(favorite)
    db.session.commit()
    
    return jsonify({"msg": "Personaje eliminado de favoritos con éxito"}), 200

# 5. Eliminar un planeta favorito
@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    current_user_id = 1  # Usuario simulado
    
    favorite = Favorite.query.filter_by(user_id=current_user_id, planet_id=planet_id).first()
    
    if favorite is None:
        return jsonify({"msg": "El planeta no está en tus favoritos"}), 404
        
    db.session.delete(favorite)
    db.session.commit()
    
    return jsonify({"msg": "Planeta eliminado de favoritos con éxito"}), 200