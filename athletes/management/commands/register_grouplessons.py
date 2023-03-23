from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Register athletes for grouplessons'

    def add_arguments(self, parser):
        parser.add_argument('Register athletes: ', nargs='*', type=str, help='Register athletes for grouplessons')

    def handle(self, *args, **options):
        self.stdout.write(f'Register athletes: {options["Register athletes: "]}')

        if len(options["Register athletes: "]) >= 1:
            self.stdout.write(self.style.SUCCESS('The athletes are registered successfully!'))
        else:
            raise CommandError("You didn't register any athlete, is that right?\
                   \nIf so, enter again the command: python manage.py register_groupslessons")
            