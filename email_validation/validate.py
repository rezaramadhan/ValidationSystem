from bs4 import BeautifulSoup

import requests

cookie = ""

def init_connection():
    url = "http://verify-email.org/"
    r = requests.get(url)
    cookie = r.headers['Set-Cookie'].split(";")[0]
    soup = BeautifulSoup(r.text, 'lxml')
    form = soup.find_all("input", type="hidden", value="1")[0].get('name')
    return (cookie,form)

def validate_email(email_checked):
    (cookie, form) = init_connection()
    print cookie
    print form

    url = "http://verify-email.org/index.php?option=com_emailverifier&view=emailverifier&layout=verify&format=raw&check="
    # email_checked = "testest@gmail.com"
    url = url + email_checked + "&" + form + "=1"
    print url

    headers = {'Cookie': cookie}

    print
    r = requests.get(url, headers=headers)
    print r.text
    soup = BeautifulSoup(r.text, 'lxml')
    # soup = BeautifulSoup('<div class="resultsBox"> \
    # 		<div class="alert alert-block alert-error  fade in"> \
    # 			<a class="close" data-dismiss="alert" href="#">&times;</a> \
    # 			<p><h3>bounce@gmail.com - Result: Bad</h3></p> \
    # 		</div> \
    # 		<pre>MX record about gmail.com exists.<br/>Connection succeeded to alt4.gmail-smtp-in.l.google.com SMTP.<br/>220 mx.google.com ESMTP l19si14100773qtf.37 - gsmtp<br/> \
    # &gt; HELO verify-email.org <br/>250 mx.google.com at your service<br/> \
    # &gt; MAIL FROM: &lt;check@verify-email.org&gt;<br/>=250 2.1.0 OK l19si14100773qtf.37 - gsmtp<br/> \
    # &gt; RCPT TO: &lt;bounce@gmail.com&gt;<br/>=550-5.1.1 The email account that you tried to reach does not exist. Please try<br/> \
    # 550-5.1.1 double-checking the recipient\'s email address for typos or<br/> \
    # 550-5.1.1 unnecessary spaces. Learn more at<br/> \
    # 550 5.1.1  https://support.google.com/mail/?p=NoSuchUser l19si14100773qtf.37 - gsmtp<br/> \
    # </pre> \
    # 	</div> \
    # ', 'lxml')
    resultHeader = soup.find_all("h3")[0].findAll(text=True)[0]
    result = resultHeader.find("Result: ")
    return not(resultHeader[result + 8:] == "Bad")

# print "requesting"
# print url
#
# r  = requests.get(url)
# print "request done"
# data = r.text
#
# print data

# soup = BeautifulSoup(data)
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
