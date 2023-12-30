import smtplib
import email.mime.text
import email.header
import email.mime.multipart

def sendEmail(to_addr,filename):
    """
    @功能  :发送邮件的功能
    """
    content = email.mime.multipart.MIMEMultipart()
    files = email.mime.text.MIMEText(open(filename,"rb").read(),"base64","utf-8")
    files["Content-Type"] = "application/octet-stream"
    files["Content-Disposition"] = "attachment;filename=testReport.html"
    content.attach(files)
    content['From'] = email.header.Header("张三","utf-8")
    content["To"] = email.header.Header("李四","utf-8")
    content["Subject"] = email.header.Header("测试报告","utf-8")

    client = smtplib.smtp()
    client.connect("smtp.163.com",25)
    client.login("email","password")
    client.sendmail("email",to_addr,content.as_string())