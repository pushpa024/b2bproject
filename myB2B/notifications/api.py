from django.core.mail import EmailMessage


class EmailNotification:
    def __init__(self):
        self._message = ""
        self._subject = ""
        self._sender = ""
        self._receivers = []
        self._bcc_list = []
        self._reply_to = []
        self._headers = {}
        self._email_message = EmailMessage

    @property
    def sender(self):
        return self._sender

    @property
    def message(self):
        return self._message

    @property
    def subject(self):
        return self._subject

    @property
    def receivers(self):
        return self._receivers

    @property
    def reply_to(self):
        return self._reply_to

    @property
    def bcc_list(self):
        return self._bcc_list

    @property
    def headers(self):
        return self._headers

    @sender.setter
    def sender(self, value):
        self._sender = value

    @subject.setter
    def subject(self, value):
        self._subject = value

    @message.setter
    def message(self, value):
        self._message = value

    @receivers.setter
    def receivers(self, value):
        self._receivers = value

    @reply_to.setter
    def reply_to(self, value):
        self._reply_to = value

    @bcc_list.setter
    def bcc_list(self, value):
        self._bcc_list = value

    @headers.setter
    def headers(self, value):
        self._headers = value

    def send(self):
        email = self._email_message(
            self._subject,
            self._message,
            self._sender,
            self._receivers,
            self._bcc_list,
            self._reply_to,
        )
        email.content_subtype = 'html'
        email.send()





