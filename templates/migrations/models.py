from django.db import models

class Card(models.Model):
    Value = models.IntegerField(validators=[
            MaxValueValidator(13),
            MinValueValidator(1)                     #From 1 to 13 (A to K)
        ], primary_key=True)
    Suit = models.CharField(max_length=8, primary_key=True, choices=(
            ("D", "Diamonds"),
            ("H", "Hearts"),
            ("C", "Clubs"),
            ("S", "Spades")
        )
    ) #Suit(Diamonds,Hearts,Clubs or Spades)
    Image = Image #The actual Card Image
class Image(models.Model):
    ImageID = models.IntegerField(primary_key=True) #Image unique identifier
    Name = models.CharField() #Alias
    Link = models.CharField() #Link for the image

