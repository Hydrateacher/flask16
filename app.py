from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')
def index():    
    return render_template('index.html')



@app.route('/park', methods=['GET', 'POST'])
def park():
    price=None
    error=None
    if request.method == 'POST':        
        yosh = int(request.form.get('are'))            
        if yosh <= 4:                
            error = "Yosh bolalarga bepul"
        elif yosh <= 12:
            price = 5000
        elif yosh < 65:
            price = 10000
        else:
            price = 8000       

    return render_template('park.html', price=price, error=error)







@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        if len(login) > 5:
           return render_template('login.html', login=login)
        else:
            return render_template('login.html', error="Login kamida 6 ta harfdan iborat bo'lishi kerak.")    
    return render_template("login.html", error=None)














@app.route('/dust', methods=['GET', 'POST'])
def dust():
    if request.method == 'POST':
        friends = [request.form.get(f'friend{i}').title() for i in range(1, 6)]
        return render_template('dust.html', friends=friends)        
    else:
        return render_template('dust.html')





    
    

if __name__ == '__main__':
    app.run(debug=True)

