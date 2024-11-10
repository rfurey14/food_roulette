git from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

#fetch meals based on country
@app.route('/meals', methods=['GET'])
def get_meals():
    country = request.args.get('country')  # Get the country from query parameters
    if not country:
        return jsonify({'error': 'Country parameter is required'}), 400

    gen_meals_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={country}"
    response1 = requests.get(gen_meals_url)
    
    food_types = ['British', 'American', 'French', 'Canadian', 'Jamican', 'Chinese', 'Dutch', 'Greek', 'Indian', 'Irish', 
                  'Italian', 'Japanese','Malaysian', 'Mexican', 'Moroccan', 'Croatian', 'Portuguese', 
                 'Russian', 'Spanish', 'Thai']
    
    meal_pics = {} #meals and their pics
    meal_recipes = {} #meals and their recipes

    if response1.status_code == 200:
        data = response1.json()
        if data.get('meals'):
            for meal in data['meals']:
                meal_name = meal['strMeal']
                meal_id = meal['idMeal']
                meal_recipes_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
                response2 = requests.get(meal_recipes_url)
                
                recipe = None
                
                if response2.status_code == 200:
                    recipe_data = response2.json()
                    if recipe_data and 'meals' in recipe_data:
                        recipe = recipe_data['meals'][0]['strInstructions']
                        meal_recipes[meal_name] = recipe
                    else:
                        print(f"No recipe found for {meal_name}")
                else:
                    print(f"Failed to fetch recipe for {meal_name}")        
                meal_pics[meal_name] = meal['strMealThumb']    
            return jsonify({
                'meal_pics': meal_pics,
                'meal_recipes': meal_recipes,
                'food_types' : food_types
            })
        else:
            return jsonify({'message': f"No meals found for {country}"}), 404
    else:
        return jsonify({'error': 'Failed to fetch data from the external API'}), 500
if __name__ == '__main__':
    app.run(debug=True)  

