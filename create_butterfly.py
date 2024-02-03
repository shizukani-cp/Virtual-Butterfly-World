import os, shizukani, json

def create_butterfly(**components):
    dir = "butterflyDatas/" + shizukani.randomfname(10)
    os.mkdir(dir)
    data = {
            "name":components["name"],
            "characters":components["characters"],
            "location":components["location"],
            "vectol":components["vectol"],
            "direction":components["direction"],
            "positional":components["positional"],
            "LM":components["LM"]
            }
    with open(dir + "/components.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data,indent=4))

if __name__ == "__main__":
    pass
    """create_butterfly(name=input("name > "),characters=input("characters > ").split(","))"""