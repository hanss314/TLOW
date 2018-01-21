def reason():
    setup = "_/O\_ <(What's wrong?)$ -|- $ / \\"
    punchline = "  O   <(Well, mal-COME here and see!)$ -|- $ / \\"
    for z in range(2):
        print(["Sally", setup, "Malcolm", punchline][z*2] + ":")
        print(["Sally", setup, "Malcolm", punchline][z*2+1].replace("$", "\n"))
    raise OverflowError("Cringiness beyond acceptable levels. Computer shutting down.")

reason()