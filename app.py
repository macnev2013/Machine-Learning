import subprocess
p = subprocess.Popen("systemctl status mysql", stdout = subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p.status = p.wait()
ans = "running" in output
if(ans == False):
	print "MySql is down :("
	print "Retrying"
	p = subprocess.Popen("systemctl restart mysql", stdout = subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
print "output :" , ans


