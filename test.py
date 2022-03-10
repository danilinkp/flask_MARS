from requests import get, post, delete

print(post('http://localhost:5000/api/news').json())  # пустой запрос

print(post('http://localhost:5000/api/news',
           json={'job': 'my_job'}).json())  # передано только название работы

print(post('http://localhost:5000/api/news',
           json={'job': 'deployment of residential modules 1 and 2',
                 'team_leader_id': 1,
                 'work_size': 15,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())  # работа с таким id уже есть

print(post('http://localhost:5000/api/news',
           json={'job': 'my job',
                 'team_leader_id': 1,
                 'work_size': 10,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())


print(get('http://localhost:8080/api/jobs').json())

print(get('http://localhost:8080/api/jobs/1').json())

print(get('http://localhost:8080/api/jobs/999').json())

print(get('http://localhost:8080/api/jobs/q').json())

print(delete('http://localhost:8080/api/jobs').json())

print(delete('http://localhost:8080/api/jobs/999').json())

print(delete('http://localhost:8080/api/jobs/1').json())

print(get('http://localhost:8080/api/jobs').json())