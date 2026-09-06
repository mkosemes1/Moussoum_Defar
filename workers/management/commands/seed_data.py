from django.core.management.base import BaseCommand
from workers.models import Country, Language


class Command(BaseCommand):
    help = 'Seed countries and languages'

    def handle(self, *args, **options):
        languages_data = [
            ('wo', 'Wolof', 'West Africa'),
            ('fr', 'French', 'West Africa'),
            ('en', 'English', 'Global'),
            ('pcm', 'Pidgin', 'West Africa'),
            ('ha', 'Hausa', 'West Africa'),
            ('sw', 'Swahili', 'East Africa'),
            ('sh', 'Sheng', 'East Africa'),
            ('ak', 'Akan', 'West Africa'),
            ('am', 'Amharic', 'East Africa'),
            ('bm', 'Bambara', 'West Africa'),
            ('yo', 'Yoruba', 'West Africa'),
            ('ig', 'Igbo', 'West Africa'),
            ('zu', 'Zulu', 'Southern Africa'),
            ('af', 'Afrikaans', 'Southern Africa'),
            ('rw', 'Kinyarwanda', 'East Africa'),
            ('sn', 'Shona', 'Southern Africa'),
        ]

        for code, name, region in languages_data:
            lang, created = Language.objects.get_or_create(
                code=code,
                defaults={'name': name, 'region': region}
            )
            status = 'CREATED' if created else 'EXISTS'
            self.stdout.write(f'  {status}: {lang}')

        countries_data = [
            ('SN', 'Senegal', 'FCFA', ['Orange Money', 'Wave', 'MTN MoMo']),
            ('NG', 'Nigeria', 'NGN', ['OPay', 'PalmPay', 'MTN MoMo', 'Airtel Money']),
            ('KE', 'Kenya', 'KES', ['M-Pesa', 'Airtel Money', 'T-Kash']),
            ('GH', 'Ghana', 'GHS', ['MTN MoMo', 'Vodafone Cash', 'Airtel Money']),
            ('CI', 'Ivory Coast', 'FCFA', ['Orange Money', 'MTN MoMo', 'Wave']),
            ('ML', 'Mali', 'FCFA', ['Orange Money', 'Wave']),
            ('CM', 'Cameroon', 'XAF', ['MTN MoMo', 'Orange Money']),
            ('TZ', 'Tanzania', 'TZS', ['M-Pesa', 'Tigo Pesa', 'Airtel Money']),
            ('ET', 'Ethiopia', 'ETB', ['Telebirr', 'CBE Birr']),
            ('ZA', 'South Africa', 'ZAR', ['SnapScan', 'Zapper', 'FNB eWallet']),
        ]

        for code, name, currency, mobile_money in countries_data:
            country, created = Country.objects.get_or_create(
                code=code,
                defaults={
                    'name': name,
                    'currency': currency,
                    'mobile_money_services': mobile_money,
                }
            )
            status = 'CREATED' if created else 'EXISTS'
            self.stdout.write(f'  {status}: {country}')

        # Link languages to countries
        links = {
            'SN': ['wo', 'fr'],
            'NG': ['en', 'pcm', 'ha', 'yo', 'ig'],
            'KE': ['sw', 'en', 'sh'],
            'GH': ['en', 'ak'],
            'CI': ['fr'],
            'ML': ['fr', 'bm'],
            'CM': ['fr', 'en'],
            'TZ': ['sw', 'en'],
            'ET': ['am', 'en'],
            'ZA': ['zu', 'af', 'en'],
        }

        for country_code, lang_codes in links.items():
            country = Country.objects.get(code=country_code)
            langs = Language.objects.filter(code__in=lang_codes)
            country.languages.set(langs)
            self.stdout.write(f'  Linked {country}: {[l.name for l in langs]}')

        self.stdout.write(self.style.SUCCESS('Done!'))
