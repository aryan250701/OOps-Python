class EmainService: 
    
    def __init__(self,userName, recieverName):
        self.userName = userName
        self.recieverName = recieverName
        pass
    
    def _authenticate(self):
        # Authentication logic here
        print(f"Authenticating user: {self.userName}")
        return True  # Assuming authentication is successful
    def _autthenticateReciever(self):
        print(f"Authenticating reciever: {self.recieverName}")
        return True
    
    def sendEmail(self):
        if self._authenticate() and self._autthenticateReciever():
            print(f"Email sent from {self.userName} to {self.recieverName}")
        else:
            print("Authentication failed. Email not sent.")


email = EmainService("aryan","swagatika")
email.sendEmail()