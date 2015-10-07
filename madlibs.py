from random import choice

from flask import Flask, render_template, request, flash, redirect


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)
app.secret_key = 'secretkey'

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    person = request.args["person"]

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=person, compliment=compliment)

# route for game
@app.route('/game')
def show_game_form():

    person =  request.args.get("person")

    if request.args.get("play") == "no":
        return render_template('goodbye.html', person=person)
    else:
        return render_template('game.html', person=person)

@app.route('/madlib', methods = ["POST"])
def show_madlib():

    person = request.form.get("person")
    name = request.form.get("name")
    color = request.form.get("color")
    noun = request.form.get("noun") 
    adjectives = request.form.getlist("adjectives")  
    randomlib = choice(["madlib.html", "madlib_2.html"])

    # if the user doesn't type in anything:
    if not name:
        flash("please type in a name")

    else: 
        return render_template(randomlib, 
                           person=person, 
                           name=name, 
                           color=color, 
                           noun=noun, 
                           adjectives=adjectives,
                           )

    return(redirect("/game"))

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
