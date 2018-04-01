from flask import Flask, request, make_response, redirect, render_template
import sys

app = Flask(__name__)

userPass = {'alice':'ilikemoney', 'bob':'password', 'jeremy':'jeremy', 
        'ralph':'watchdog', 'todd':'toddFather', 'admin':'Admini$trator'}

bobFriends = ['alice', 'jeremy', 'ralph', 'todd']

coins = {'bob': 50, 'alice': 100, 'jeremy': 50, 'ralph': 50, 'todd': 100}

''' Default page, landing page, directs user to login page. '''
@app.route('/')
def home():
        return render_template('login.html') # load the login page

''' Potential guide for the site??? '''
@app.route('/welcome')
def welcome():
    return render_template('welcome.html') # render the template

''' login page redirects to this, upon successful login, loads next page '''
@app.route('/login', methods=['GET','POST'])
def login():
    cook = request.cookies.get('username')
    if cook and cook in userPass.keys():
        # successful login
        if cook == 'bob':
            resp = make_response(render_template('loggedIn.html', 
                username=cook, friends=bobFriends, coin=coins[cook]))
        elif cook == 'admin':
            resp = make_response(render_template('loggedIn.html', 
                username=cook))
        else:
            resp = make_response(render_template('loggedIn.html', 
                username=cook, coin=coins[cook]))
        resp.set_cookie('username', cook)
        return resp
    # no cookie, check to see if parameters were sent
    elif request.form != None:
        user = request.form['username']
        passwd = request.form['password']
        # if there is no cookie, but a username and password
        if user in userPass and userPass[user] == passwd:
            # successful login w/ username bob
            if user == 'bob':
                resp = make_response(render_template('loggedIn.html', 
                    username=user, friends=bobFriends, coin=coins[user]))
            # successful login, username not bob
            else:
                resp = make_response(render_template('loggedIn.html', 
                    username=user, coin=coins[user]))
            resp.set_cookie('username', user)
            return resp
        # if the username and password are incorrect
        else:
            error = 'Invalid credentials.'
            return render_template('login.html', error=error)
    # if cookies are not correct
    else:
        error = 'Invalid credentials.'
        return render_template('login.html', error=error)

''' Transfer coins between the current user and someone else '''
@app.route("/transfer", methods=['GET','POST'])
def transfer():
    cook = request.cookies.get('username')
    # if user exists, we can trade
    if cook and cook in userPass.keys():
        user = request.form['username']
        amount = int(request.form['amount'])
        #print amount
        print type(amount)
        if cook == 'admin':
            coins[user] = coins[user] + amount
            resp = make_response(render_template('loggedIn.html', 
                trasnfer=True, tCoins=amount, tUser=user, username=cook))
            resp.set_cookie('username', cook)
            return resp
        elif coins[cook] >= 0:
            coins[user] = coins[user] + amount
            coins[cook] = coins[cook] - amount
            if coins[user] <= 0:
                resp = make_response(render_template('loggedIn.html', 
                    trasnfer=True, tCoins=amount, tUser=user, username=cook,
                    debt=True, coin=coins[cook]))
                resp.set_cookie('username', cook)
            else:
                resp = make_response(render_template('loggedIn.html', 
                    trasnfer=True, tCoins=amount, tUser=user, username=cook, 
                    coin=coins[cook]))
                resp.set_cookie('username', cook)
            return resp
        else:
            error = 'Transactoin failed. Please try again.'
            resp = make_response(render_template('loggedIn.html', error=error,
               username=cook))
            resp.set_cookie('username', cook)
            return resp

if __name__ == "__main__":
	app.run(host='0.0.0.0')
