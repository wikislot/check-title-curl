from lxml import html
import requests

domains = open("domains.txt","r")
jobs = len(list(domains))
jobcount = 0
domains = open("domains.txt","r")
for domain in domains:
	try:
		page = requests.get('https://'+domain.rstrip("\r\n"))
		tree = html.fromstring(page.content)
		open('report.csv','a').write(domain.rstrip("\r\n")+','+str(tree.xpath('//title/text()')[0])+'\n')
		jobcount+=1
		print(domain.rstrip("\r\n")+','+str(tree.xpath('//title/text()')[0]))
		print('jobs left= '+str(int(jobs)-int(jobcount)))
	except:
		open('report.csv','a').write(domain.rstrip("\r\n")+',EROR\n')
		jobcount+=1
		print(domain.rstrip("\r\n")+',EROR')
		print('jobs left= '+str(int(jobs)-int(jobcount)))
print('done')
input('Press Enter to exit')
