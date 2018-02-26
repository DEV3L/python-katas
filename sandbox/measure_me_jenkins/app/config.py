from app.dao.os_env import os_environ

jenkins_url = 'http://jenkins-ci.route53.osstage.net:8080/'

github_login_url = 'https://github.com/login'

github_username = os_environ('GITHUB_USERNAME', default='github_username')
github_password = os_environ('GITHUB_PASSWORD', default='github_password')

webpage_cache_path = './data/web_pages/'
