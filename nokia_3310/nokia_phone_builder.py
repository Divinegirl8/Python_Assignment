# now lets enhance this code so it doesnt break
# if run this and enter a character instead of number what happens??

def menu():
    user_phone = int(input("""
        MENU
press 1 -->   Phone book
press 2 -->   Messages
press 3 -->   Chat
press 4 -->   Call Register
press 5 -->   Tones
press 6 -->   Settings
press 7 -->   Call Divert
press 8 -->   Games
press 9 -->   Calculator
press 10 -->  Reminders
press 11 -->  Clock
press 12 -->  Profiles
press 13 -->  SIM services
                       
"""))

    match user_phone:
        case 1:
            phone_book()

        case 2:
            message()

        case 3:
            chat()

        case 4:
            call()

        case 5:
            tone()

        case 6:
            settings()

        case 7:
            call_divert()

        case 8:
            games()

        case 9:
            calculator()

        case 10:
            reminders()

        case 11:
            clock()

        case 12:
            profiles()

        case 13:
            sim_services()

        case _:
            menu()


def phone_book():
    phone = int(input("""
    Phone Book
press 1 --> Search
press 2 --> Service Nos
press 3 --> Add Name
press 4 --> Erase
press 5 --> Edit
press 6 --> Assign tone
press 7 --> Send B' Card
press 8 --> Options
press 9 --> Speed Dials
press 10 --> Voice Tags
press 11 --> Exit     
    """))
    match phone:
        case 1:
            print("search")
        case 2:
            print("Service Nos")
        case 3:
            print("Add Name")
        case 4:
            print("Erase")
        case 5:
            print("Edit")
        case 6:
            print("Assign tone")
        case 7:
            print("Send B' Card")
        case 8:
            options()
        case 9:
            print("Speed Dials")
        case 10:
            print("Voice Tags")
        case 11:
            menu()
        case _:
            phone_book()


def options():
    option_user = int(input("""
        Options
press 1 --> Type of view
press 2 --> Memory status
press 3 --> Go back to previous menu
press 4 --> Exit  
 
    """))

    match option_user:
        case 1:
            print("type of view")
        case 2:
            print("memory status")
        case 3:
            phone_book()
        case 4:
            menu()
        case _:
            options()


def message():
    user_message = int(input("""
        Message
press 1 --> Compose a message
press 2 --> Inbox
press 3 --> View saved messages
press 4 --> Picture messages
press 5 --> Templates
press 6 --> Smileys
press 7 --> Message settings
press 8 --> Info service
press 9 --> Voice mailbox number
press 10 --> Service command editor
press 11 --> Exit         

    """))

    match user_message:
        case 1:
            print("compose a message")
        case 2:
            print("inbox")
        case 3:
            print("view saved messages")
        case 4:
            print("picture message")
        case 5:
            print("templates")
        case 6:
            print("smileys")
        case 7:
            message_setting()
        case 8:
            print("info service")
        case 9:
            print("Voice mailbox number")
        case 10:
            print("Service command editor")
        case 11:
            menu()
        case _:
            message()


def message_setting():
    message_set = int(input("""
Message Settings
press 1 --> Set
press 2 --> Common
press 3 --> Go back to previous menu
press 4 --> Exit    
     
    """))
    match message_set:
        case 1:
            set_user()
        case 2:
            common()
        case 3:
            message()
        case 4:
            menu()
        case _:
            message_setting()


def set_user():
    set_use = int(input("""
         Set
press 1 --> Message Centre Number
press 2 --> Message sent as
press 3 --> Message validity
press 4 --> Go back to the previous menu
press 5 --> Exit   
    
    """))
    match set_use:
        case 1:
            print("Message Centre Number")
        case 2:
            print("Message sent as")
        case 3:
            print("Message validity")
        case 4:
            message_setting()
        case 5:
            menu()
        case _:
            set_user()


def common():
    common_user = int(input("""
        Common
press 1 --> Delivery Report
press 2 --> Reply via same centre
press 3 --> Character support
press 4 --> Go back to the previous menu
press 5 --> Exit   
   
   """))

    match common_user:
        case 1:
            print("Delivery Report")
        case 2:
            print("Reply via same centre")
        case 3:
            print("Character support")
        case 4:
            message_setting()
        case 5:
            menu()
        case 6:
            common()


def chat():
    chat_user = int(input("""
       Chat
press 1 --> Compose a message
press 2 --> Chat history
press 3 --> Chat name
press 4 --> Exit   
     """))

    match chat_user:
        case 1:
            print("Compose a message")
        case 2:
            print("Chat history")
        case 3:
            print(" Chat name")
        case 4:
            menu()
        case _:
            chat()


def call():
    calls = int(input("""
        Calls
press 1 --> Missed calls
press 2 --> Received calls
press 3 --> Dialled numbers
press 4 --> Erased recent call lists
press 5 --> Show call duration
press 6 --> Show call costs
press 7 --> Call cost setting
press 8--> Prepaid credit
press 9 --> Exit     
    """))
    match calls:
        case 1:
            print("Missed calls")
        case 2:
            print("Received calls")
        case 3:
            print("Dialled numbers")
        case 4:
            print("Erased recent call lists")
        case 5:
            print("Show call duration")
        case 6:
            print("Show call costs")
        case 7:
            print("Call cost setting")
        case 8:
            print("Prepaid credit")
        case 9:
            menu()
        case _:
            call()


def tone():
    tones = int(input("""
       Tones
press 1 --> Ringing tone
press 2 --> Ringing volume
press 3 --> Incoming call alert
press 4 --> Composer
press 5 --> Message alert tone
press 6 --> Keypad tones
press 7 --> Warning and games tones
press 8 --> Vibrating alert
press 9 --> Screen saver
press 10 --> Exit  
    
   """))
    match tones:
        case 1:
            print("Ringing tone")
        case 2:
            print("Ringing volume")
        case 3:
            print("Incoming call alert")
        case 4:
            print("Composer")
        case 5:
            print("Message alert tone")
        case 6:
            print("Keypad tones")
        case 7:
            print("Warning and games tones")
        case 8:
            print("Vibrating alert")
        case 9:
            print("Screen saver")
        case 10:
            menu()
        case _:
            tone()


def settings():
    setting_user = int(input("""
    Setting
press 1 --> Call settings
press 2 --> Phone settings
press 3 --> Security settings
press 4 --> Restore factory settings
press 5 --> Exit    
      
    """))
    match setting_user:
        case 1:
            call_setting()
        case 2:
            phone_setting()
        case 3:
            security_setting()
        case 4:
            print("restore factory setting")
        case 5:
            menu()
        case _:
            settings()


def call_setting():
    call_user = int(input("""
    Call Setting
press 1 --> Automatic redial
press 2 --> Speed dialling
press 3 --> Call waiting options
press 4 --> Own number sending
press 5 --> Phone line in use
press 6 --> Automatic answer
press 7 --> Go back to previous menu
press 8 --> Exit       
    
    """))
    match call_user:
        case 1:
            print("Automatic redial")
        case 2:
            print("Speed dialling")
        case 3:
            print("Call waiting options")
        case 4:
            print("Own number sending")
        case 5:
            print("Phone line in use")
        case 6:
            print("Automatic answer")
        case 7:
            settings()
        case 8:
            menu()
        case _:
            call_setting()


def phone_setting():
    phone_user = int(input("""
 Phone Setting
press 1 --> Language
press 2 --> Cell info display
press 3 --> Welcome note
press 4 --> Network selection
press 5 --> Lights
press 6 --> Confirm SIM service actions
press 7 --> Go back to previous menu
press 8 --> Exit   
     
    """))
    match phone_user:
        case 1:
            print("Language")
        case 2:
            print("Cell info display")
        case 3:
            print("Welcome note")
        case 4:
            print("Network selection")
        case 5:
            print("Lights")
        case 6:
            print("Confirm SIM service actions")
        case 7:
            settings()
        case 8:
            menu()
        case _:
            phone_setting()


def security_setting():
    security_user = int(input("""
  Security Setting  
press 1 --> PIN code request
press 2 --> Call barring service
press 3 --> Fixed dialling
press 4 --> Closed user group
press 5 --> Phone security
press 6 --> Change access codes
press 7 --> Go back to previous menu
press 8 --> Exit   
    
    """))

    match security_user:
        case 1:
            print("PIN code request")
        case 2:
            print("Call barring service")
        case 3:
            print("Fixed dialling")
        case 4:
            print("Closed user group")
        case 5:
            print("Phone security")
        case 6:
            print("Change access codes")
        case 7:
            settings()
        case 8:
            menu()
        case _:
            security_setting()


def call_divert():
    print("call divert")


def games():
    print("games")


def calculator():
    print("calculator")


def reminders():
    print("reminders")


def clock():
    clock_user = int(input("""
       Clock
press 1 --> Alarm clock
press 2 --> Clock settings
press 3 --> Date setting
press 4 --> Stopwatch
press 5 --> Countdown timer
press 6 --> Auto update of date and time
press 7 --> Exit    
    
    """))
    match clock_user:
        case 1:
            print("Alarm clock")
        case 2:
            print("Clock settings")
        case 3:
            print("Date setting")
        case 4:
            print("Stopwatch")
        case 5:
            print("Countdown timer")
        case 6:
            print("Auto update of date and time")
        case 7:
            menu()
        case _:
            clock()


def profiles():
    print("profiles")


def sim_services():
    print("SIM services")