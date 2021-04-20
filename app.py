from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    phrase_lower = phrase.lower()
    letters = request.form['letters']
    result = str(search4letters(phrase_lower, letters))
    last_result = result.strip("{'}")
    title = 'Here are your results:'
    return render_template('results.html', the_results=last_result, the_phrase=phrase, the_letters=letters, the_title=title)


@app.route('/')
@app.route('/entry')    
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the Web")



if __name__ == '__main__':
    app.run(debug=True)

