from flask import Flask, render_template, request, redirect, url_for, session
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
app.secret_key = "smartbiz_secret_key"

# MySQL Connection
connection = pymysql.connect(
    host='centerbeam.proxy.rlwy.net',
    user='root',
    password='BBheZZtUEOhhqdHKyYkXflvHyTIhSnXa',
    database='railway',
    port=54429
)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = connection.cursor()

        query = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"

        cur.execute(query, (name, email, password))

        connection.commit()

        cur.close()

        return "User Registered Successfully!"

    return render_template('signup.html')


#Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        cur = connection.cursor()

        query = "SELECT * FROM users WHERE email=%s AND password=%s"

        cur.execute(query, (email, password))

        user = cur.fetchone()

        cur.close()

        if user:

            session['user'] = user[1]

            return redirect(url_for('dashboard'))

        else:
            return "Invalid Email or Password"

    return render_template('login.html')

#Dashboard
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect(url_for('login'))

    cur = connection.cursor()

    # Total Users
    cur.execute("SELECT COUNT(*) FROM users")
    total_users = cur.fetchone()[0]

    # Revenue Data
    cur.execute("SELECT month, amount FROM revenue")

    revenue_data = cur.fetchall()

    months = []
    amounts = []

    for row in revenue_data:

        months.append(row[0])
        amounts.append(row[1])

    # Revenue Growth Calculation

    if len(amounts) >= 2:

        previous = amounts[-2]
        current = amounts[-1]

        revenue_growth = round(
            ((current - previous) / previous) * 100,
            2
        )

    else:

        revenue_growth = 0

    cur.close()

    return render_template(

        'dashboard.html',

        total_users=total_users,

        username=session['user'],

        months=months,

        amounts=amounts,

        revenue_growth=revenue_growth

    )
 
 #Analytics   
@app.route('/analytics')
def analytics():

    if 'user' not in session:
        return redirect(url_for('login'))

    cur = connection.cursor()

    # Total Projects
    cur.execute("SELECT COUNT(*) FROM projects")
    total_projects = cur.fetchone()[0]

    # Revenue Data
    cur.execute("SELECT month, amount FROM revenue")
    revenue_data = cur.fetchall()

    cur.close()

    return render_template(
        'analytics.html',
        total_projects=total_projects,
        revenue_data=revenue_data
    )
    
#Report
@app.route('/reports')
def reports():

    if 'user' not in session:
        return redirect(url_for('login'))

    cur = connection.cursor()

    # Fetch project data
    cur.execute("""
        SELECT project_name,
               project_status,
               deadline
        FROM projects
    """)

    report_data = cur.fetchall()

    # Total Projects
    cur.execute("SELECT COUNT(*) FROM projects")
    total_projects = cur.fetchone()[0]

    # Completed Projects
    cur.execute("""
        SELECT COUNT(*)
        FROM projects
        WHERE project_status='Completed'
    """)

    completed_projects = cur.fetchone()[0]

    # Revenue Growth (Static Example)
    revenue_growth = "+18%"

    cur.close()

    return render_template(
        'reports.html',
        reports=report_data,
        total_projects=total_projects,
        completed_projects=completed_projects,
        revenue_growth=revenue_growth
    )
    
#Logout    
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect(url_for('login'))

#Project Route
@app.route('/projects', methods=['GET', 'POST'])
def projects():

    if request.method == 'POST':

        project_name = request.form['project_name']
        project_status = request.form['project_status']
        deadline = request.form['deadline']

        cur = connection.cursor()

        query = """
        INSERT INTO projects(project_name, project_status, deadline)
        VALUES(%s, %s, %s)
        """

        cur.execute(query, (project_name, project_status, deadline))

        connection.commit()

        cur.close()

        return redirect(url_for('projects'))

    cur = connection.cursor()

    cur.execute("SELECT * FROM projects")

    all_projects = cur.fetchall()

    cur.close()

    return render_template(
        'projects.html',
        projects=all_projects
    )
           
#Delete
@app.route('/delete_project/<int:id>')
def delete_project(id):

    cur = connection.cursor()

    query = "DELETE FROM projects WHERE id=%s"

    cur.execute(query, (id,))

    connection.commit()

    cur.close()

    return redirect(url_for('projects'))

#Edit
@app.route('/edit_project/<int:id>', methods=['GET', 'POST'])
def edit_project(id):

    cur = connection.cursor()

    if request.method == 'POST':

        project_name = request.form['project_name']
        project_status = request.form['project_status']
        deadline = request.form['deadline']

        query = """
        UPDATE projects
        SET project_name=%s,
            project_status=%s,
            deadline=%s
        WHERE id=%s
        """

        cur.execute(
            query,
            (project_name, project_status, deadline, id)
        )

        connection.commit()

        cur.close()

        return redirect(url_for('projects'))

    query = "SELECT * FROM projects WHERE id=%s"

    cur.execute(query, (id,))

    project = cur.fetchone()

    cur.close()

    return render_template(
        'edit_project.html',
        project=project
    )
    
    


if __name__ == '__main__':
    app.run(debug=True)