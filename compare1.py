class message:
    def __init__(self,text,date,sender):
        self.text=text
        self.date=date
        self.sender=sender
messages= [
    message("hii",10,"manoj"),
    message("hii1",11,"manu"),
    message("hii2",12,"man")
]
for msg in messages:
    print(vars(msg))
new=message("hi",10,"noj")
is_found=False
for msg in messages:
    if msg.text==new.text and msg.sender==new.sender:
        is_found=True
if not is_found:
    print(messages.append(new))
    print("succesfully added new list item")

        