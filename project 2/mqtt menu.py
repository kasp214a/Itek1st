
selection = input("would you like to access the moodboard press 1 for chat Chat press 2 or hangmand press 3")

if selection == ("2"):
        from mqttchat import main
        print ("you are now in the chat mode")
        main()

elif selection == ("1"):
        from mqttmood import mood
        print ("you are now in the mood mode")
        mood()

elif selection == ("3"):
        from hangman import main
        print ("you are in the hangman mode")
        main()


















