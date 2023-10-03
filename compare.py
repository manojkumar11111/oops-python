class Message:
    def __init__(self,message_text,message_sender):
        self.message_text=message_text
        self.message_sender=message_sender
    def compare(self,other):
        if isinstance(other,Message):
            return self.message_text==other.message_text and self.message_sender==other.message_sender
        else:
            return False
        
message=[
    Message("hii","manoj"),
    Message("hello","gulla")
]

new_message=Message("hmm","manu")
is_found=any([msg.compare(new_message) for msg in message])

if not is_found:
    message.append(new_message)
    print("new message added to list")
for msg in message:
    print(vars(msg))