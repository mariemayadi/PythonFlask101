#from flask import Flask
from flask import Flask, render_template

#refering to data.py
from data import Articles

#Create an instance of the flask class
app = Flask(__name__)

#Articles() refers to the function within data.py, which returns a set of articles
Articles = Articles()

#creating a route in flask - will most likely return a template
@app.route('/')
def index():
	#return 'INDEX'
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	#return render_template('articles.html')
	# Add a second param in order to include the data later looped through in the html
	return render_template('articles.html', articles = Articles)



# In this case, ID is a dynamic value, thus the <string:id> + need to pass into the function
@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id=id)


if __name__ == '__main__':
	#app.run()
	# To see changes 
	app.run(debug=True)