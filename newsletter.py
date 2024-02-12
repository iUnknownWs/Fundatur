import smtplib
import requests
from dateutil import parser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
from pathlib import Path
import os
env_path = Path('.') / '.env'
load_dotenv(env_path)

response = requests.get('https://iunknownws.pythonanywhere.com/blogpost/')

if response.status_code == 200:
    data = response.json()
else:
    print("Error:", response.status_code)

count = 0
countimg = 0
sender_email = 'noticiasfundatur@gmail.com'
receiver_email = ['willders.carvajal@gmail.com', 'giuliogaro2@gmail.com']
subject = "Newsletter Fundatur Eventos"
body = """
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
  <title></title><!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style type="text/css">
    #outlook a {padding: 0;}

    .ReadMsgBody {
      width: 100%;
    }

    .ExternalClass {
      width: 100%;
    }

    .ExternalClass * {
      line-height: 100%;
    }

    body {
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    table,
    td {
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

    img {
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
      -ms-interpolation-mode: bicubic;
    }

    p {
      display: block;
      margin: 13px 0;
    }
  </style><!--[if !mso]><!-->
  <style type="text/css">
    @media only screen and (max-width:480px) {
      @-ms-viewport {
        width: 320px;
      }

      @viewport {
        width: 320px;
      }
    }
  </style><!--<![endif]--><!--[if mso]>
        <xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG/>
          <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
        </xml>
        <![endif]--><!--[if lte mso 11]>
        <style type="text/css">
          .outlook-group-fix { width:100% !important; }
        </style>
        <![endif]-->
  <style type="text/css">
    @media only screen and (min-width:480px) {
      .mj-column-px-500 {
        width: 500px !important;
        max-width: 500px;
      }

      .mj-column-px-450 {
        width: 450px !important;
        max-width: 450px;
      }

      .mj-column-px-220 {
        width: 220px !important;
        max-width: 220px;
      }

      .mj-column-px-300 {
        width: 300px !important;
        max-width: 300px;
      }
    }
  </style>
  <style type="text/css">
    @media only screen and (max-width:480px) {
      table.full-width-mobile {
        width: 100% !important;
      }

      td.full-width-mobile {
        width: auto !important;
      }
    }
  </style>
</head>

<body>
  <div>
    <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style="background:#fff;background-color:#fff;Margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
        style="background:#fff;background-color:#fff;width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:5px;text-align:center;vertical-align:top;">
              <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:500px;" ><![endif]-->
              <div class="mj-column-px-500 outlook-group-fix"
                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                  width="100%">
                  <tr>
                    <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                        style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:200px;"><img alt="logo" height="auto" src="cid:icon"
                                style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;"
                                width="200"></td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </table>
              </div><!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style="background:#ffffff;background-color:#ffffff;Margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
        style="background:#ffffff;background-color:#ffffff;width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:20px 0 0 0;text-align:center;vertical-align:top;">
              <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:450px;" ><![endif]-->
              <div class="mj-column-px-450 outlook-group-fix"
                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                  <tbody>
                    <tr>
                      <td style="vertical-align:top;padding:0;">
                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                          <tr>
                            <td align="center" style="font-size:0px;padding:0;word-break:break-word;">
                              <div
                                style="font-family:Helvetica;font-size:13px;line-height:1;text-align:center;color:#000000;">
                                Hola Buen dia, Aquí te presentamos una selección de los últimos eventos</div>
                            </td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div><!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    """
for blog in data:
    count += 1
    if count > 5:
        break
    date = blog['publishDate']
    date_obj = parser.parse(date)
    dt = date_obj.strftime('%d/%m/%Y')
    dynamic = f"""
    <div style="background:#ffffff;background-color:#ffffff;Margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
        style="background:#ffffff;background-color:#ffffff;width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:0px;text-align:center;vertical-align:top;">
              <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:220px;" ><![endif]-->
              <div class="mj-column-px-220 outlook-group-fix"
                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                  width="100%">
                  <tr>
                    <td align="center" style="font-size:0px;padding:15px 0 0 0;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                        style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:220px;"><img alt="car" height="auto"
                                src="cid:{blog['image_details']["id"]}"
                                style="border:0;border-radius:20px 0px;display:block;outline:none;text-decoration:none;height:auto;width:100%;"
                                width="220"></td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </table>
              </div><!--[if mso | IE]></td><td class="" style="vertical-align:top;width:300px;" ><![endif]-->
              <div class="mj-column-px-300 outlook-group-fix"
                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                  width="100%">
                  <tr>
                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table cellpadding="0" cellspacing="0" width="100%" border="0"
                        style="cellspacing:0;color:#000000;font-family:Helvetica;font-size:12px;line-height:16px;table-layout:auto;width:100%;">
                        <tbody>
                          <tr>
                            <td style="font-weight:bold;font-size:16px;" colspan="4">
                              <p style="display:inline-block;width:200px;">{blog['title']}</p>
                            </td>
                          </tr>
                          <tr>
                            <td>{dt}</td>
                          </tr>
                          <tr>
                            <td style="padding:10px 0 25px 0;font-weight:400;font-size:12px" colspan="4">{blog['description']}</td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </table>
              </div><!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    """
    body += dynamic
body += """
    <!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style="background:#ffffff;background-color:#ffffff;Margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
        style="background:#ffffff;background-color:#ffffff;width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:15px 0 15px 0;text-align:center;vertical-align:top;">
              <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:500px;" ><![endif]-->
              <div class="mj-column-px-500 outlook-group-fix"
                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                  width="100%">
                  <tr>
                    <td align="center" vertical-align="middle"
                      style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                        style="border-collapse:separate;width:300px;line-height:100%;">
                        <tr>
                          <td align="center" bgcolor="transparent" role="presentation"
                            style="border:1px solid #000;border-radius:50px;cursor:auto;padding:10px 25px;background:transparent;"
                            valign="middle"><a href="https://fundatur.netlify.app/blog/"
                              style="background:transparent;color:#000000;font-family:Helvetica;font-size:13px;font-weight:bold;line-height:120%;Margin:0;text-decoration:none;text-transform:none;"
                              target="_blank">Ir al Blog</a></td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </div><!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
    <div style="background:#fff;background-color:#fff;Margin:0px auto;max-width:600px;">
      <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation"
        style="background:#fff;background-color:#fff;width:100%;">
        <tbody>
          <tr>
            <td style="direction:ltr;font-size:0px;padding:10px 0 0 0;text-align:center;vertical-align:top;">
              <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:500px;" ><![endif]-->
              <div class="mj-column-px-500 outlook-group-fix"
                style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                  width="100%">
                  <tr>
                    <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                      <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                        style="border-collapse:collapse;border-spacing:0px;">
                        <tbody>
                          <tr>
                            <td style="width:200px;"><img alt="logo" height="auto" src="cid:icon"
                                style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;"
                                width="200"></td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </table>
              </div><!--[if mso | IE]></td></tr></table><![endif]-->
            </td>
          </tr>
        </tbody>
      </table>
    </div><!--[if mso | IE]></td></tr></table><![endif]-->
  </div>
</body>
</html>
"""

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = ', '.join(receiver_email)
msg["Subject"] = subject

msg.attach(MIMEText(body, 'html'))

with open('icon.png', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-ID', '<icon>')
    msg.attach(img)

for blog in data:
    countimg += 1
    if countimg > 5:
        break
    response = requests.get(blog['image_details']['image'])
    img_data = response.content
    img = MIMEImage(img_data)
    img.add_header('Content-ID', f'<{blog['image_details']["id"]}>')
    msg.attach(img)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, os.getenv('SMTP_PASSWORD'))
text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)
print("Email sent!")
server.quit()