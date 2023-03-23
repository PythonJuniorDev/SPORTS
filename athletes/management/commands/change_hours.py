from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Command to change temporary changed opening hours!\
            \ne.g. 31 01 2023 10:00-18:00 New Year\'s Eve Happy new year!'


    def add_arguments(self, parser):
        parser.add_argument('Day:', type=str, help='Fill in the day')
        parser.add_argument('Month:', type=str, help='Fill in the month')
        parser.add_argument('Year:', type=str, help='Fill in the year')
        parser.add_argument('Changed opening hours:', type=str, help='Please enter in this order: day, month, year, effective date')
        parser.add_argument('--Public_holiday: ', nargs='*', default='does not apply', type=str, help='Optional possibility to enter public holiday')
        parser.add_argument('--Add_message: ', nargs='*', default='does not apply', type=str, help='Optional possibility to enter message')
        
       
    def handle(self, *args, **options):                
        print(f'Day: {options["Day:"]}')
        print(f'Month: {options["Month:"]}')
        print(f'Year: {options["Year:"]}')
        print(f'Change in the opening hours: {options["Changed opening hours:"]}')
        print('Public holiday: ', end='')

        for i in options["Public_holiday: "]:
            print(i, end=' ')

        print('\nMessage: ', end='')
        for i in options["Add_message: "]:
            print(i, end=' ')



        # print(f'{options["Add_message: "]}')
        # self.stdout.write(f'Public holiday: {options["Public_holiday: "]}')

        # if options["Add_message: "]:
        #     self.stdout.write(self.style.SUCCESS('Option2 is TRUE'))
        # else:
        #     self.stdout.write(self.style.WARNING('Option 2 is FALSE'))



        # https://www.youtube.com/watch?v=V0RfgNIwCqI