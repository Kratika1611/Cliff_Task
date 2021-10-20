from flask import Flask, json ,Response,request
from flask.wrappers import Response 
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host= "localhost",
        port= 5001
    )
    mongo.server_info()
    db = mongo.admin
    print("Connected")
except:
    print("ERROR - Cannot connect to db")

@app.route("/insert",methods =["POST"])
def create_user():
    try: 
        data = {
        "name":request.form["name"],
        "brand_name": request.form["brand_name"],
        "regular_price_value" : request.form["regular_price_value"],
        "offer_price_value": request.form["offer_price_value"],
        "currency": request.form["currency"],
        "classification_l1": request.form["classification_l1"],
        "classification_l2": request.form["classification_l1"],
        "image_url": request.form["image_url"]
        }
        
        dbRes = db.test.insert_one(data)
        print(dbRes.inserted_id)
        return Response(
            response= json.dumps(
                { "message:" "Data Inserted" }
            )
        )

    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps(
                {"message:" "Data not inserted"}
            )
        )

@app.route("/getdata", methods=["GET"])  
def get_data():
    try:
      data = list(db.test.find())
      for check in data:
          check["_id"] = str(check["_id"])
      print(data)
      return Response(
          response= json.dumps(data)
      )

    except Exception as ex:  
        print(ex) 
        return Response(
            response= json.dumps(
                {"message:" "Data not found"}
            )
        )

@app.route("/update/<id>", methods=["PATCH"])
def update_data(id):
    try:
       dbRes = db.test.update_one(
           {"_id":ObjectId(id)},
           {"$set":{"name": request.form["name"]}}
        )
       if dbRes.modified_count ==1:
            return Response(
                response= json.dumps(
                    {"message": "user updated"}
                )
            )  
       else:
            return Response(
                response= json.dumps(
                    {"message":"nothing to update"}
                )
            )  
    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps(
                {"message": "sorry cannot update data"}
            )
        )


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
