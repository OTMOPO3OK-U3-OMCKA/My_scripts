from flask import Flask
from classes import candidates_list, Candidates
candidates = candidates_list('candidates.json')
our_cand = Candidates(candidates)

app = Flask(__name__)

@app.route("/")
def get_pre():
    st = """Имя кандидата - name
Позиция кандидата - position
Навыки через запятую - skills
"""
    ls =[]
    for i in our_cand.candidates:
        st1 = st.replace('name', i['name'])
        st1 = st1.replace('position', i['position'])
        st1 = st1.replace('skills', i['skills'])
        ls.append('<pre>'+st1+'</pre>')
    return ''.join(ls)

@app.route("/candidates/<x>")
def get_candidates(x):
    return our_cand.id_candidate(x)

@app.route("/skills/<x>")
def get_skills(x):
    return our_cand.name_list_with_skills(x)

app.run()

