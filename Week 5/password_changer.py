username = input("Please enter your username: ")
student_id = input("Please enter your student ID: ")
banned_list = [username, student_id, "huddersfield", "justinbieber" , "cheese", "canalside"]
changed = False

while changed is False:
    new_pass = input("Please enter a password: ")
    confirm_pass = input("Please confirm your password: ")
    if new_pass == confirm_pass and len(new_pass) in range(6, 12) and new_pass not in banned_list:
        print("Password changed.")
        changed = True
    else:
        print("Password not changed. Please try again.")
