from flask import Flask, render_template, request
from utils import *

candidates = get_candidates('candidates.json')


app = Flask(__name__)

@app.route('/')

def list_name():
    name_cand = load_candidates_from_json(candidates)
    return render_template('list.html', name_cand=name_cand)

@app.route('/candidate/<x>')
def get_id_candidate(x):
    name = ''
    position = ''
    image = ''
    skills = ''
    for i in candidates:
        if i['id'] == int(x):
            name = i['name']
            position = i['position']
            image = i['picture']
            skills = i['skills']
    return render_template('card.html',
                           name=name,
                           position=position,
                           image=image,
                           skills=skills)

@app.route('/search/<candidate_name>')
def search(candidate_name):
    list_candidates = get_candidates_by_name(candidate_name, candidates)
    count = len(list_candidates)
    return render_template('search.html',
                           list_candidates=list_candidates, count=count)

@app.route('/skill/<skill_name>')
def skill(skill_name):
    list_candidates = get_candidates_by_skill(skill_name, candidates)
    count = len(list_candidates)
    return render_template('skill.html',
                           list_candidates=list_candidates,
                           count=count,
                           skill_name=skill_name)

app.run()

