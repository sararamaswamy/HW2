## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number. Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.
import requests
import json


from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'


@app.route('/question',methods= ['POST','GET'])
def enter_number():
	s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/result" method="GET">
  Enter your favorite number:<br>
  <input type="text
  " name="thenumber" value="">
  <br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>""" # Note that this defaults to first name is Mickey, last name is Mouse -- you could change that!
	return s

@app.route('/result',methods = ['POST', 'GET'])
def res():
    if request.method == 'GET':
      ## Get it from the above method shown in the html. if making a GET request to this place, get request. args, a way of accessing the arguments requested. (data)
        result = request.args
        ## args 
        num = result.get('thenumber')
        double_num = float(num) * 2
        printable_num = str(double_num)


        # return render_template("result.html",result = result)
        ## GET request got sent to the result route/result place. if the request method was GET, this means the GET request sent some stuff here, can get argumetns from the GET request and pull them out by their names. can show them on a page and render them in the same way. 
        return "<b>" + "Double your number is" + "</b>, <i>" + printable_num + "</i>" 


## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application. It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. If a user has to select a radio button representing a song name, it should do a search for that song in an API.
# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)



## [PROBLEM 2]
@app.route('/music',methods= ['POST','GET'])
def enter_song():
    s = """<!DOCTYPE html>
<html>
<body>

<form action="http://localhost:5000/result/artistname" method="GET">
  Who sang the song titled "Closer"?:<br>
  <input type="radio" name="artist" value="Demi Lovato" checked> Demi Lovato<br>
  <input type="radio" name="artist" value="Bruce Springsteen"> Bruce Springsteen<br>
  <input type="radio" name="artist" value="The Chainsmokers"> The Chainsmokers <br>
  <input type="submit">
</form> 

</body>
</html>""" 
    return s

@app.route('/result/artistname',methods = ['POST', 'GET'])
def music_view():
    if request.method == 'GET':
    	result = request.args
    	artistname = result.get('artist')
    	if artistname == "Demi Lovato":
    		response_display = "Try Again! Hint: They played in New York City in August, 2018."
    	if artistname == "Bruce Spingsteen":
    		response_display = "Try Again! Hint: They played in New York City in August, 2018."
    	if artistname == "The Chainsmokers":
    		response_display = "Correct! You've got a good ear."
    	return response_display



    	# artistname = artistname
    	# baseurl = "https://itunes.apple.com/search"

    	# # artist_name = result.get('artist')
    	# params = {"entity": "music", "term": artistname}
    	# resp = requests.get(baseurl,params=params)
    	# data_text = resp.text
    	# python_obj = json.loads(data_text)
    	# data_return = json.dumps(python_obj, indent = 2)
    	# print(data_return)
    	# return data_return


        # return render_template("result.html",result = result)
        ## GET request got sent to the result route/result place. if the request method was GET, this means the GET request sent some stuff here, can get argumetns from the GET request and pull them out by their names. can show them on a page and render them in the same way. 











