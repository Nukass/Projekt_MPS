from flask import Flask, render_template, request, redirect, url_for, session

import pymysql

app = Flask(__name__)
app.secret_key = 12

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='pythonlogin')

cur = conn.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        msg = ''
        username = request.form['username']
        password = request.form['password']
        cur.execute("select * from accounts where username=%s and password= %s", (username, password))
        if cur.rowcount > 0:
            for row in cur:
                account = row
            if account:
                return render_template('profile.html', msg=account)
        else:
            msg = 'Nespravne uzivatelske jmeno/heslo'
            return render_template('index.html', msg=msg)


    else:

        return render_template('index.html', msg='')


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cur.execute("insert into accounts values(%s, %s, %s, %s)", (None, username, password, email))
        # cur.execute("SELECT * FROM accounts")
        # print(cur)
        # for row in cur:
        #     print(row)
        msg = "Prosim prihlaste se pro pokracovani..."
        return render_template('index.html', msg=msg)

    elif request.method == 'POST':
        msg = 'Vyplnte prosim formular!'
    return render_template('register.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
