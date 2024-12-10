from flask import Blueprint, render_template, request, jsonify
from app import db
import openai
from flask_login import login_required

openai.api_key = os.getenv('OPENAI_API_KEY')

bp = Blueprint('chat', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('index.html')

@bp.route('/ask', methods=['POST'])
@login_required
def ask():
    user_input = request.form['user_input']

    if not user_input.strip():
        return jsonify({'response': 'Пожалуйста, введите вопрос.'})

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        gpt_response = response.choices[0].text.strip()
        return jsonify({'response': gpt_response})
    except Exception as e:
        return jsonify({'response': f'Ошибка при обработке запроса: {str(e)}'})
