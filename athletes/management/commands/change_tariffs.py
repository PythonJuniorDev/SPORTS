from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Inform the athletes about changed tariffs.'

    def add_arguments(self, parser):
        parser.add_argument('Old tariff: ', type=float, help='Fill in old tariff')
        parser.add_argument('New tariff: ', type=float, help='Fill in new tariff')
        parser.add_argument('Rate effective date: ', type=str, help='Fill in start date new tariff')

    
    def handle(self, *args, **options):
        print(f'Old tariff: {options["Old tariff: "]}')
        print(f'New tariff: {options["New tariff: "]}')
        print(f'Rate effective date: {options["Rate effective date: "]}')
            

        if options["Old tariff: "] < options["New tariff: "]:
            self.stdout.write(self.style.SUCCESS('Tariff changed succesfully.'))
        else:
            raise CommandError('The new tariff is less than the old tariff. Is that right?\
                               \nIf not enter again the command: python manage.py change_tariffs')  
 
