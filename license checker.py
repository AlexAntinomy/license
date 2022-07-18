print ('Hello!')
def check_status(age, license):
    if int(age) > 18 and int(license) == 1:
        print(' You are good to go, initiating systems')
    elif int(age) < 18:
        print('Hell no, your are still a kid!')
    elif not license == 1:
        print(' Get a license dude!, I will not run')
    return check_status
