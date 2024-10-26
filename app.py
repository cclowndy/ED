from flask import Flask, render_template, request
from EmotionDetect.emotion_detection import emotion_detector
from EmotionDetect.emotion_detection import emotion_predictor



app = Flask(__name__)

def run():
    app.run(host="0.0.0.0", port=8080)
    

@app.route('/emotionDetector')

def send_detector():
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return(
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )
    
@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == "__main_":
    run()