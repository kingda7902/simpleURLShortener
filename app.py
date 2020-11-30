from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/<redirect_id>')
def index(redirect_id=None):
    if redirect_id:
        return redirect('https://www.google.com')
    return render_template('shortener.html')


@app.route('/post/<post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/shortify', methods=['POST'])
def shortify():
    return {'short_link': 'test'}


if __name__ == '__main__':
    app.debug = True
    app.run()
