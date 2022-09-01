if __name__ == "__main__":
    sisters = ("Luna", "Alexa", "Siri")
    brothers = ("John", "Jimmy")
    siblings = sisters + brothers
    print("Siblings: "+str(len(siblings)))
    family_members = siblings + ("Father", "Mother")
    print("Family members: " + str(family_members))
