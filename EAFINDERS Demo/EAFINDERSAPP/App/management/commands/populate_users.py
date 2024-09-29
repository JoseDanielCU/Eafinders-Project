import random
from django.core.management.base import BaseCommand
from App.models import Usuario  # Replace 'App' with the actual name of your app if it's different
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with 50 random users'

    # List of valid careers
    CARRERAS = [
        'Ingenieria de Sistemas',
        'Ingenieria de Diseño de Producto',
        'Ingenieria Mecanica',
        'Ingenieria Fisica',
        'Ingenieria Matematica',
        'Ingenieria Civil',
        'Gastronomia',
        'Psicologia',
        'Geologia',
        'Musica',
        'Negocios Internacionales',
        'Biologia',
        'Comunicación Social',
        'Derecho',
        'Economia',
    ]

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(50):
            nombres = fake.first_name()
            apellidos = fake.last_name()
            # Generate email with eafit.edu.co domain
            email = f"{nombres.lower()}.{apellidos.lower()}@eafit.edu.co"
            password = 'Password123'  # Set a default password for all users

            usuario = Usuario(
                nombres=nombres,
                apellidos=apellidos,
                email_institucional=email,
                password=password,
                foto_perfil='perfil_fotos/default.jpg',  # Adjust this if you have a default image
                biografia=fake.paragraph(),
                carrera=random.choice(self.CARRERAS),  # Choose a random career from the list
                semestre=random.randint(1, 10)  # Random semester between 1 and 10
            )
            usuario.set_password(password)
            usuario.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 50 users.'))
