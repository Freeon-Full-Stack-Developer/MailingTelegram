app = Flask(__name__)
webbrowser.open('http://127.0.1:5000/')
@app.route('/', methods=['GET', 'POST'])
def run():

    if request.method == 'POST':
        token = request.form.get('token')
        text = request.form.get('text')
        path = request.form.get('path_file')

        if token or text or path != "":
            bot = telebot.TeleBot(token)
            def send_mess(message, path):

                try:
                    cols = [0]
                    top_players = pd.read_excel(path, usecols=cols)
                    print(top_players.head(1))

                    for index, row in top_players.iterrows():
                        user_id = row[0]
                        bot.send_message(user_id, message)

                except Exception as e:
                    return jsonify({'error': str(e)})

            send_mess(text, path)
            return render_template('index.html')

        else:
            return render_template('index.html')

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
