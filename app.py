import subprocess
p = subprocess.Popen("systemctl status mysql", stdout = subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p.status = p.wait()
ans = "running" in output
print "output :" , ans

