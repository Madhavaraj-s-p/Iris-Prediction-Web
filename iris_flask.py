#importing
from flask import Flask,redirect,url_for,render_template,request,flash,get_flashed_messages,session

#In this code,we creating instance of class Flask with __name__  which is default shortcut for rendering template and locate url
app = Flask(__name__)
app.secret_key = "Madhavaraj"

@app.route('/')
@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        global Sepel_W,Sepel_L,Petal_L,Petal_W,pred

        Sepel_L = request.form.get('Sepel_Length')
        Sepel_W = request.form.get('Sepel_Width')
        Petal_L = request.form.get('Sepel_Length')
        Petal_W = request.form.get('Petal_Width')

        print(f'Sepel Length is {Sepel_L}')
        print(f'Sepel Widht is {Sepel_W}')
        print(f'Petal Length is {Petal_L}')
        print(f'Petal Widht is {Petal_W}')

        global sl,sw,pl,pw
        sl = float(Sepel_L) #type: ignore
        sw = float(Sepel_W) #type: ignore
        pl = float(Petal_L) #type: ignore
        pw = float(Petal_W) #type: ignore
    
        from iris import Iris

        I = Iris()
        print(I.iris_run(sl,sw,pl,pw))

        pred = I.iris_run(sl,sw,pl,pw)

        session['sl'] = sl
        session['sw'] = sw
        session['pl'] = pl
        session['pw'] = pw
        session['pred'] = pred

        return redirect(url_for('result'))

        return render_template("Iris_page1_html.htm",pred = pred)
    return render_template('Iris_page1_html.htm')

@app.route('/result')
def result():
    global sl,sw,pl,pw,pred

    sl = session.get('sl')
    sw = session.get('sw')
    pl = session.get('pl')
    pw = session.get('pw')
    pred = session.get('pred')

    sl = f"Sepel Length:{sl}"
    sw = f"Sepel Width:{sw}"
    pl = f"Petal Length:{pl}"
    pw = f"Petal Width:{pw}"
    pred =pred
    return render_template('Iris_page2_html.htm',sl = sl,sw = sw,pw = pw,pl = pl,pred = pred)
    
if __name__ == '__main__': 
    app.run(debug=True)