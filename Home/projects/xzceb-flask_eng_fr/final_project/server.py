# from machinetranslation import translator
from flask import Flask, render_template, request,jsonify
import json
from machinetranslation import english_tofrench,french_toenglish

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    res=english_tofrench(textToTranslate)
 
    return "Translated text to French: \t{}".format(res)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    res=french_toenglish(textToTranslate)
    return "Translated text to English: \t {}".format(res)

@app.route("/")
def renderIndexPage():
 return render_template("index.html")  # Write the code to render template
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
