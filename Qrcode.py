from flask import Flask, request, redirect
import qrcode
import user_agents

app = Flask(__name__)


PLAY_STORE_URL = "https://play.google.com/store/apps/details?id=com.googlesignexbee&hl=en_IN"
APP_STORE_URL = "https://apps.apple.com/in/app/huntsjob-overseas-job-search/id6738483906"

#test whether the application is running
@app.route('/helloworld')
def helloworld():
    return "Hello, World!"

@app.route('/')
def redirect_user():
    ua_string = request.headers.get('User-Agent')
    ua = user_agents.parse(ua_string)

    if ua.os.family == "Android": 
        return redirect(PLAY_STORE_URL)
    elif ua.os.family == "iOS": 
        return redirect(APP_STORE_URL)
    else:
        return redirect("https://www.huntsjob.com/")

def generate_qr():
    url = "http://192.168.4.214:5000"  # Change if deploying online
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save("app_qr.png")
    print(" QR code generated and saved as app_qr.png")

if __name__ == '__main__':
    generate_qr()
    app.run(host="0.0.0.0", port=5000, debug=True)  # Accessible across network
