from django.db import models
class IP(models.Model):
	ip_address=models.GenericIPAddressField(protocol='both', unpack_ipv4=False)
	#ip_address = models.IPAddressField()
	create_time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
        		return self.ip_address

class Picture(models.Model):
	pic_name = models.CharField(max_length=30)
	path=models.FileField(upload_to='./upload/')
	def __unicode__(self):
        		return self.pic_name

class Dream(models.Model):
	ip = models.ForeignKey(IP)
	picture = models.OneToOneField(Picture)
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	content = models.TextField()
	love_num = models.IntegerField(default=0)
	create_time = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.name
