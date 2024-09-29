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

    # Sample phrases for each career
    CARRERA_BIOGRAFIAS = {
        'Ingenieria de Sistemas': "Me apasiona desarrollar software y me encanta resolver problemas complejos con código. En mi tiempo libre, disfruto jugar videojuegos.",
        'Ingenieria de Diseño de Producto': "Me interesa mucho el diseño de productos innovadores. Disfruto crear prototipos y en mi tiempo libre me gusta pintar.",
        'Ingenieria Mecanica': "Me fascina cómo funcionan las máquinas y disfruto mucho el diseño de motores. En mi tiempo libre, me gusta andar en bicicleta.",
        'Ingenieria Fisica': "Me encanta explorar los misterios del universo a través de la física. En mi tiempo libre, disfruto leer libros de ciencia ficción.",
        'Ingenieria Matematica': "Soy un apasionado por las matemáticas aplicadas y la investigación. En mi tiempo libre, disfruto resolver acertijos matemáticos.",
        'Ingenieria Civil': "Me gusta diseñar estructuras seguras y funcionales. En mi tiempo libre, disfruto caminar por la ciudad admirando la arquitectura.",
        'Gastronomia': "Me encanta experimentar con sabores y crear nuevas recetas. En mi tiempo libre, disfruto probar restaurantes locales.",
        'Psicologia': "Me interesa mucho comprender el comportamiento humano y ayudar a las personas. En mi tiempo libre, disfruto leer sobre psicología.",
        'Geologia': "Me fascina estudiar la tierra y los procesos que la moldean. En mi tiempo libre, disfruto hacer senderismo.",
        'Musica': "La música es mi pasión, ya sea interpretando o componiendo. En mi tiempo libre, disfruto asistir a conciertos.",
        'Negocios Internacionales': "Me encanta el comercio global y entender cómo interactúan las economías. En mi tiempo libre, disfruto viajar y conocer nuevas culturas.",
        'Biologia': "Me interesa mucho la vida en todas sus formas, desde lo más pequeño hasta lo más grande. En mi tiempo libre, disfruto cuidar plantas.",
        'Comunicación Social': "Me apasiona comunicar ideas de manera efectiva y generar impacto en la sociedad. En mi tiempo libre, disfruto escribir en mi blog.",
        'Derecho': "Me fascina el derecho y cómo podemos usarlo para construir una sociedad más justa. En mi tiempo libre, disfruto leer novelas de misterio.",
        'Economia': "Me interesa comprender cómo funcionan los mercados y las decisiones económicas. En mi tiempo libre, disfruto analizar tendencias económicas.",
    }

    def handle(self, *args, **kwargs):
        fake = Faker('es_ES')  # Configuración de Faker para español
        for _ in range(50):
            nombres = fake.first_name()
            apellidos = fake.last_name()
            # Generate email with eafit.edu.co domain
            email = f"{nombres.lower()}.{apellidos.lower()}@eafit.edu.co"
            password = 'Password123'  # Set a default password for all users
            carrera = random.choice(self.CARRERAS)
            biografia = self.CARRERA_BIOGRAFIAS.get(carrera, fake.paragraph())

            usuario = Usuario(
                nombres=nombres,
                apellidos=apellidos,
                email_institucional=email,
                password=password,
                foto_perfil='perfil_fotos/default.jpg',  # Adjust this if you have a default image
                biografia=biografia,
                carrera=carrera,  # Choose a random career from the list
                semestre=random.randint(1, 10)  # Random semester between 1 and 10
            )
            usuario.set_password(password)
            usuario.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 50 users.'))
