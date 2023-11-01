from flask import Flask, render_template, request
import requests
import smtplib

BLOG_URL = 'https://api.npoint.io/14d011b1142a61417233'

post_response = requests.get(BLOG_URL).json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', blogs=post_response)


@app.route('/about')
def about_me():
    return render_template('about.html')


@app.route('/contact')
def contact_me():
    return render_template('contact.html')


@app.route('/post/<int:blog_id>')
def view_blog(blog_id):
    read_blog = None
    for blog in post_response:
        if blog['id'] == blog_id:
            read_blog = blog
            break
    return render_template('post.html', blog=read_blog)


my_mail = 'gomagiftk01@gmail.com'


@app.route('/form-entry', methods=['post'])
def send_email():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_mail, password='tpseeplsqniiijjc')
        connection.sendmail(from_addr=my_mail,
                            to_addrs='giftian.kg@gmail.com',
                            msg=f'subject: sender info\n\n'
                                f' name: {request.form["your_name"]}\n\n'
                                f'contact: {request.form["your_number"]}\n\n'
                                f'message: {request.form["your_message"]}'

                            )
    return f'<h1> {"sent successfully"} </h1>'


if __name__ == '__main__':
    app.run(debug=True)
