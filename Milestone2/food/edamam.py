from flask import Blueprint, jsonify, flash
#from utils.api import API
from sql.db import DB
import json
from datetime import datetime

edamam = Blueprint('edamam', __name__, url_prefix='/edamam')

@edamam.route("/update", methods=["GET"])
def update():
    #rv437 and 12/14/23
    result = update_edamam()
    return result

def update_edamam():
    #rv437 and 12/14/23
    url = "/api/food-database/v2/parser"
    querystring = {"nutrition-type": "cooking", "category[0]": "generic-foods", "health[0]": "alcohol-free"}
    response = API.get(url, querystring)
    print("API Response:", response)
    print("Response Type:", type(response))

    if response:
        #rv437 and 12/14/23
        try:
            if isinstance(response, str):
                response = json.loads(response)
                print("Response after loading as JSON:", response)

            if isinstance(response, dict):
                data = response.get('data',[])

                if isinstance(data, list) and data:
                    query = """
                        INSERT INTO Food (
                             Url, Label, Enerc_Kcal, Protein, Fat, Carbohydrate, Fiber,
                            Category, Weight, Created, Modified
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                            Url = VALUES(Url),
                            Label = VALUES(Label),
                            Enerc_Kcal = VALUES(Enerc_Kcal),
                            Protein = VALUES(Protein),
                            Fat = VALUES(Fat),
                            Carbohydrate = VALUES(Carbohydrate),
                            Fiber = VALUES(Fiber),
                            Category = VALUES(Category),
                            Weight = VALUES(Weight),
                            Modified = VALUES(Modified)
                    """

                    food_data = []

                    for food_item in data:
                        #rv437 and 12/14/23
                        food_values = (
                            
                            food_item.get('Url'),
                            food_item.get('Label'),
                            food_item.get('Enerc_Kcal'),
                            food_item.get('Protein'),
                            food_item.get('Fat'),
                            food_item.get('Carbohydrate'),
                            food_item.get('Fiber'),
                            food_item.get('Category'),
                            food_item.get('Weight'),
                            datetime.now(),
                            datetime.now()
                        )
                        food_data.append(food_values)

                    print("SQL Query:", query)
                    print("Food Data:", food_data)

                    DB.insertOne(query, food_data)  # Assuming you have a DB class/module with this method
                    print(f"Inserted {len(data)} records to the Food table")

                    return jsonify(response)
                else:
                    return jsonify(error="No data found in the response."), 500
            else:
                return jsonify(error="Unexpected response format. 'data' key not found."), 500

        except Exception as e:
            #rv437 and 12/14/23
            print(str(e))
            flash(f"An error occurred: {str(e)}", "danger")
            return jsonify(error=str(e)), 500

    else:
        return jsonify(error="Unexpected response format"), 500