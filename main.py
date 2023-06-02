from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            content = file.read().decode('utf-8')
            words = content.lower().split()
            frequency = {}

            for word in words:
                if word.isalpha():
                    if word in frequency:
                        frequency[word] += 1
                    else:
                        frequency[word] = 1

            if len(frequency) > 0:
                most_frequent_word = max(frequency, key=frequency.get)
                return render_template('result.html', word=most_frequent_word, frequency=frequency[most_frequent_word])
            else:
                return 'No words were found in the file.'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)