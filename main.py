# Import back-endove knihovny pro backend
from flask import Flask, render_template, request, redirect, url_for, session

# Import knihovny pro komunikaci s databazi
import pymysql

# Inicializace back-endove knihovny
app = Flask(__name__)
app.secret_key = 12

# Pripojeni k databazi
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='pythonlogin')

# Ziskani ukazatele pro manipulaci s databazi
cur = conn.cursor()

# Tato cesta slouzi pro prihlasovani a zaroven pro domovskou stranku
@app.route('/', methods=['GET', 'POST'])
def login():
    # Pokud jsme poslali formular a obsahuje vsechny potrebne hodnoty muzeme se zkusit prihlasit
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        msg = ''
        
        # Ziskame potrebne udaje z formulare
        username = request.form['username']
        password = request.form['password']
        
        # Overime jestli existuje ucet se shodujicim heslem a jmenem
        cur.execute("select * from accounts where username=%s and password= %s", (username, password))
        
        # Pokud existuje tak zobrazime domovskou stranku s udaji
        if cur.rowcount > 0:
            for row in cur:
                account = row
            if account:
                return render_template('profile.html', msg=account)
        # Pokud ne tak zobrazime chybovou hlasku
        else:
            msg = 'Nespravne uzivatelske jmeno/heslo'
            return render_template('index.html', msg=msg)

    # Pokud jsme neposlali formular, znamena to, ze chceme zobrazit prihlasovaci stranku
    else:
        return render_template('index.html', msg='')

# Tato cesta slouzi pro odhlaseni
@app.route('/logout')
def logout():
    # Smazeme vsechny ulozene sessions
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    
    # Presmerujeme na prihlasovaci stranku
    return redirect(url_for('login'))

# Tato cesta slouzi k registraci
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    # Zkontrolujeme jestli se poslal formular a overime jestli obsahuje vsechny potrebne udaje
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Ziskame vsechny hodnoty z formulare
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # Vlozime do databaze
        cur.execute("insert into accounts values(%s, %s, %s, %s)", (None, username, password, email))
        
        # Zobrazime prihlasovaci obrazovku
        msg = "Prosim prihlaste se pro pokracovani..."
        return render_template('index.html', msg=msg)
    
    # Pokud jsme poslali formular, ale neobsahuje vsechny potrebne udaje, tak zobrazime chybovou hlasku
    elif request.method == 'POST':
        msg = 'Vyplnte prosim formular!'
        
    # Pokud jsme zadny formular neposlali, tak to znamena, ze teprve chceme zobrazit registracni stranku
    return render_template('register.html', msg=msg)

# Spusteni cele aplikace
if __name__ == '__main__':
    app.run(debug=True)
