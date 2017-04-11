from locust import HttpLocust, TaskSet


urls = []
f = open('/root/ayasakov/hosts.txt', 'r')
for line in f:
    if 'http' in line:
        urls.append('{}'.format(line[:-1]))

print urls


def getting_page(l):
    for url in urls:
        l.client.get(url, name=url)


class UserBehavior(TaskSet):
    tasks = {getting_page: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
