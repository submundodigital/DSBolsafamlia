
from fabric.api import env,puts, run

def production():
	env.hosts = ['host1.domain.com']
	env.user = 'user'

def update():
	start = time.time()
	run('comand')
	final = time.time()
	total = final - start 
	puts('Fim...' %total)

def upgrade():
	start = time.time()
	run('comand')
	....
	...