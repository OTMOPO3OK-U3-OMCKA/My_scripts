import json

def candidates_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates

class Candidates:
    def __init__(self, cnds):
        self.candidates = cnds
        
        
    def name_list_with_skills(self, skill):
        skills = []
        skill = skill.lower()
        for i in self.candidates:
            sk = i['skills'].split(', ')
            if skill in sk or skill.title() in sk or skill.upper() in sk:
                skills.append(f"""<pre>Имя кандидата - {i["name"]}
Позиция кандидата - {i["position"]}
Навыки через запятую - {i["skills"]}</pre>""")
        return ''.join(skills)

    
    def id_candidate(self, x):
        candidate = 0
        for i in self.candidates:
            if i["id"] is int(x):
                candidate = i
                break
        return """<img src="""+candidate["picture"]+f""">
<pre>
Имя кандидата - {candidate["name"]}
Позиция кандидата - {candidate["position"]}
Навыки через запятую - {candidate["skills"]}
</pre>"""
