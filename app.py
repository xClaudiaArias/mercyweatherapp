from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city') # grabbing the location from the html form

        #get json data for location forecast using our api key and create object
        r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=abd5e96892f1e75b669c32cf6161bfbc')
        
        json_object = r.json()

        # convert data into variables 
        temperature = int((json_object['main']['temp']-273.15)*(9/5) + 32) 
        low = int(json_object['main']['temp_min']-273.15) 
        high = int(json_object['main']['temp_max']-273.15) 
        humidity = int(json_object['main']['humidity'])
        pressure = int(json_object['main']['pressure'])
        visibility = int(json_object['visibility'])
        wind = int(json_object['wind']['speed'])
        w_description = json_object['weather'][0]['description']
        icon = json_object['weather'][0]['icon']


        # print(icon)
        return render_template('index.html',temperature=temperature, low=low, high=high, visibility=visibility, pressure=pressure,humidity=humidity,city_name=city_name,wind=wind, w_description=w_description, icon=icon)
    else:
        return render_template('index.html') 


if __name__ == '__main__':
    app.run(debug=True)
