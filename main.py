import steam

import time

steam.api.key.set('FB22ABDD88A7A653434553E731344007')

help_flag = True

program_flag = False

while help_flag == True:

    print('') # print empty line for neatness

    print('Type in S to start the program.')

    print('Type in H to display help.')

    print('Type in Q to quit the program.')

    print('') # print space for neatness, prevent clumping of output

    user_input = input('Please enter your option: ')

    user_input = user_input.upper()

    if user_input == 'S':

        program_flag = True

    elif user_input == 'H':

        print('') # print line for neatness

        print('This program will alert you to the states of a player on Steam. It will refresh at your set interval.')

        print('') # print extra line for neatness

        program_flag = False

    elif user_input == 'Q':

        help_flag = False

        program_flag = False

    else:

        print('Your option was invalid. Please try again. ')

        program_flag = False

    while program_flag == True:

        input_steam_id = input('Please enter the 64-bit steamID you would like to use: ')

        profile = steam.user.profile(input_steam_id)

        try:

            profile.persona

        except (steam.user.ProfileNotFoundError):

            print('The profile is invalid. Please try again.')

            profile_is_valid = False

        else:

            profile_is_valid = True


        while profile_is_valid == False:

            input_steam_id = input('Please enter the 64-bit steamID you would like to use: ')

            profile = steam.user.profile(input_steam_id)

            try:

                profile.persona

            except:

                print('The profile is invalid. Please try again.')

            else:

                profile_is_valid = True

        try:

            refresh_timer = input('Please enter a refresh amount in seconds: ')

            refresh_timer = float(refresh_timer)

        except:

            print('An error has occurred. Please enter the refresh amount again. ')

            timer_input_valid = False

        else:

            timer_input_valid = True

            refresh_bln = True

        while timer_input_valid == False:

            try:

                refresh_timer = input('Please enter a refresh amount in seconds: ')

                refresh_timer = float(refresh_timer)

            except:

                print('An error has occurred. Please try again.')

                refresh_timer = input('Please enter a refresh amount in seconds: ')

            else:

                if refresh_timer == 0 or refresh_timer < 0:

                    print('The refresh value must be above 0 seconds. Please try again. ')

                    refresh_timer = input('Please enter a refresh amount in seconds. ')

                    refresh_timer = float(refresh_timer)

                else:

                    print('The refresh value is valid. Continuing program.')

                    refresh_bln = True

        while refresh_bln == True:
            
            print('')

            print('Identified user: ' +  str(profile.persona))

            print('Found profile URL: ' + str(profile.profile_url))

            print('Found user status: ' + str(profile.status))

            print('Found user persona: ' + str(profile.persona))

            print('Found user playing game: ' + str(profile.current_game))

            creation_date = profile.creation_date
            
            print('Found user creation date: ' + str(time.asctime(creation_date)))
            
            last_online = profile.last_online
            
            print('Found user last online at: ' + str(time.asctime(last_online)))
            
            print('Found user lobby ID: ' + str(profile.lobbysteamid))

            time.sleep(refresh_timer)

            print('') # prevent clumping of output
            















