import tkinter, glob, random, os, json

SYMBOLS = ".,!?"
ENCODE = "utf-8"

class Butterfly:
    def __init__(self, dir):
        self._set_component(dir)
    
    def _set_component(self, dir):
        with open(dir + "/components.json", "r", encoding=ENCODE) as f:
            components = json.loads(f.read())
        self.name = components["name"]
        self.likes = components["like"]
        self.characters = components["characters"]
        self.x = components["location"]["x"]
        self.y = components["location"]["y"]
        self.mvx = components["vectol"]["x"]
        self.mvy = components["vectol"]["y"]
        self.deafault_direction = components["direction"]
        self.parts = {item:(tkinter.PhotoImage(item)) + tuple(components["positional"][item]) for item in 
                      [os.path.basename(p)[:list(p).index(".")] for p in glob.glob("butterflyDatas/" + dir + "*.png")]}
        with open("butterflyDatas/" + dir + components["LM"], "r", encoding=ENCODE) as f1:
            with open("allLM.json", "r", encoding=ENCODE) as f2:
                LM = json.loads(f1.read()).update(f2.rad())
                self.LM = self.LM_split(LM)
        

    def LM_split(self, LM):
        return [{tuple([w.strip(SYMBOLS).lower() for w in s.split(" ")]):[{w.replace("{name}", self.name):p} for w, p in a.items()]}
                    for s, a in LM.items()]
        """for s, a in LM.items():
            c = {}
            b = tuple([w.strip(".,!?").lower() for w in s.split(" ")])
            for w in s.split(" "):
                b.append(w.strip(".,!?").lower())
            b = tuple(b)
            e = [{w.replace("{name}", self.name):p} for w, p in a.items()]
            for w, p in a.items():
                e.append({w.replace("{name}", self.name):p})
            c.update({b:e})
            self.LM.append({tuple([w.strip(".,!?").lower() for w in s.split(" ")]):[{w.replace("{name}", self.name):p} for w, p in a.items()]})"""

    def action(self):
        self._fly()
    
    def _fly(self):
        vx = random.randint(-self.mvx, self.mvx)
        vy = random.randint(-self.mvy, self.mvy)
        self.x += vx
        self.y += vy
    
    def talk(self, inp):
        inp_words = [w.strip(SYMBOLS).lower() for w in inp.split(" ")]
        ans_candidates = self.candidate(inp_words=inp_words)
        return random.choices(tuple(ans_candidates.keys()), weights=tuple(ans_candidates.values()))[0]
    
    def candidate(self, inp_words):
        ans = []
        for q in self.LM:
            c = 0
            for word in inp_words:
            	if word in q:
                    c += 1
            ans.append((q, c))
        ans_candidate = {}
        for q, c in ans:
            if q in ans_candidate.keys():
                ans_candidate.update({q:ans_candidate[q] + c})
            else:
                ans_candidate.update({q:c})
        return self.LM[random.choices(tuple(ans_candidate.keys()), weights=tuple(ans_candidate.values()))[0]]

if __name__ == "__main__":
    butterfly1 = Butterfly(glob.glob("butterflyDatas/*")[0])