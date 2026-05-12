
class Notification_Service:
    message_count = 0
    
    def __init__(self, priority):
        self.priority = priority
        self.log = []

    def send(self, sender, receiver, message):
        self.log.append((type(self).__name__, self.priority, sender, receiver, message))
        Notification_Service.message_count += 1

class Email_Notification(Notification_Service):
    
    def __init__(self, priority, from_email):
        super().__init__(priority)
        self.from_email = from_email
        
    def send(self, to_email, message):
        super().send(self.from_email, to_email, message)
        print(f'sending Email from:{self.from_email} to:{to_email}')
        print(f'priority: {self.priority} message: "{message}"')

class SMS_Notification(Notification_Service):
    
    def __init__(self, priority, from_nr):
        super().__init__(priority)
        self.from_nr = from_nr
        
    def send(self, to_nr, message):
        super().send(self.from_nr, to_nr, message)
        print(f'sending SMS from:{self.from_nr} to:{to_nr}')
        print(f'priority: {self.priority} message: "{message}"')
        
email = Email_Notification(2, 'support@company.com')
email.send('customer@email.com', 'Your report is ready')
email.send('customer@email.com', 'Update to Privacy Policy')
sms = SMS_Notification(3, '0123456789')
sms.send('001122334455', 'Update to Privacy Policy')
