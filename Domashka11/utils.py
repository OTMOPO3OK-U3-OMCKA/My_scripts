'''
- `load_candidates_from_json(path)` – возвращает список всех кандидатов
- `get_candidate(candidate_id)` – возвращает одного кандидата по его id
- `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
- `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку
'''
import json


def get_candidates(candidates):
    with open(candidates, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_candidates_from_json(path):
    list_candidates = {}
    for i in path:
        list_candidates[i['id']] = i['name']
    return list_candidates


def get_candidate(candidate_id):
    list_id = []
    for i in candidate_id:
        list_id.append(i['id'])
    return list_id


def get_candidates_by_name(candidate_name, candidates):
    names = []
    for i in candidates:
        name = i['name'].split(' ')
        if name[0].lower() == candidate_name.lower():
            names.append(i)
    return names


def get_candidates_by_skill(skill_name, candidates):
    names = []
    for i in candidates:
        skills = i['skills'].split(', ')
        if skill_name.lower() in skills or skill_name.title() in skills or skill_name.upper() in skills:
            names.append(i)
    return names
