from django.db import models


from django.db import models

# Contact Model
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    anniversary = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Phone Number Model
class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers')
    phone_type = models.CharField(max_length=10, choices=[('mobile', 'Mobile'), ('home', 'Home'), ('work', 'Work')])
    number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.phone_type}: {self.number}"

# Email Model
class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='emails')
    email_type = models.CharField(max_length=10, choices=[('primary', 'Primary'), ('secondary', 'Secondary')])
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.email_type}: {self.email}"

# Address Model
class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=10, choices=[('home', 'Home'), ('work', 'Work')])
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address_type}: {self.address}"

# Social Media Model
class SocialMedia(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='social_medias')
    platform = models.CharField(max_length=20)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.platform}: {self.url}"

# Interaction Log Model
class InteractionLog(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='interaction_logs')
    log = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interaction on {self.date}"
