from django.db import models
class IP(models.Model):
	ip_address=models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	create_time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
        		return self.ip_address

class Dream(models.Model):
	ip=models.ForeignKey(IP)
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	content = models.TextField()
	pic_name = models.CharField(max_length=30)
	pic_path=models.FileField(upload_to='./upload/')
	love_num = models.IntegerField(default=0)
	create_time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name
