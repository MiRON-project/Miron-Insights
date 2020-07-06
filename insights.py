
from github import Github
from datetime import datetime
import csv
import sys

repos = ['MIRON-Components', 'MIRON-Systems',
         'DomainModelsRepositories', 'MIRON-BehaviorRepository',
         'MIRON-DataRepository', 'ZMQServer', 'DataRepository', 'MOOD2Be',
         'MIRON-Modeling-Tools', 'MIRON-Roqme']

unique_view = ['Unique Views']
total_view = ['Views Count']
unique_clone = ['Unique Clones']
total_clone = ['Clones Count']

if __name__ == "__main__":
    a = sys.argv[1]
    g = Github(a)
    for org in g.get_user().get_orgs():
        if org.name == 'MiRoN':
            for r in repos:
                repo = org.get_repo(r)
                views = repo.get_views_traffic('week')
                unique_view.append(views.get('uniques'))
                total_view.append(views.get('count'))
                clones = repo.get_clones_traffic('week')
                unique_clone.append(clones.get('uniques'))
                total_clone.append(clones.get('count'))

    with open(datetime.today().strftime('%Y-%m-%d') + '.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([' '] + repos + ['Total'])

        writer.writerow(unique_view + [sum(unique_view[1:])])
        writer.writerow(total_view + [sum(total_view[1:])])
        writer.writerow(unique_clone + [sum(unique_clone[1:])])
        writer.writerow(total_clone + [sum(total_clone[1:])])

print(unique_view)
print(total_view)
print(unique_clone)
print(total_view)

