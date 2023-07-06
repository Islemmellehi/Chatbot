from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)
CORS(app)

model_name = "microsoft/DialoGPT-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

@app.route('/chatbot', methods=['POST', 'GET'])
def chatbot():
    if request.method == 'POST':
        user_input = request.json['input']
        
        input_ids = tokenizer.encode(user_input, return_tensors='pt')
        response = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        generated_text = tokenizer.decode(response[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

        return jsonify({'response': generated_text})
    else:
        return '''
        <h1>Welcome to the Chatbot "Spaghettita Margaritta" Endpoint!</h1>
        <p>This is a default text to know my prayers for this to work have been heard.</p>
        '''

if __name__ == '__main__':
    app.run()