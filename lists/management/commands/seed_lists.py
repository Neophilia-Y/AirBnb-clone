from django.core.management.base import BaseCommand
from lists import models as list_model
from users import models as user_model
from rooms import models as room_model
from django.contrib.admin.utils import flatten
from django_seed import Seed
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="how many reviews do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_model.User.objects.all()
        all_rooms = room_model.Room.objects.all()

        seeder.add_entity(
            list_model.List, number, {"user": lambda x: random.choice(all_users),},
        )
        list_created = seeder.execute()
        created_clean = flatten(list(list_created.values()))
        for pk in created_clean:
            new_list = list_model.List.objects.get(pk=pk)
            to_add = all_rooms[random.randint(0, 2) : random.randint(3, 6)]
            new_list.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} list created"))
