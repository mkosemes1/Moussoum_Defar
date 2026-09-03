from django.core.management.base import BaseCommand
from evaluation.models import AfricanBenchmark, TestCase
from evaluation.benchmarks import ALL_BENCHMARKS


class Command(BaseCommand):
    help = 'Charge les benchmarks africains dans la base de données'

    def handle(self, *args, **options):
        self.stdout.write('Chargement des benchmarks africains...')

        for benchmark_data in ALL_BENCHMARKS:
            benchmark, created = AfricanBenchmark.objects.get_or_create(
                country_code=benchmark_data['country_code'],
                name=benchmark_data['name'],
                version=benchmark_data['version'],
                defaults={
                    'description': benchmark_data['description'],
                    'country_name': benchmark_data['country_name'],
                    'language_code': benchmark_data['language_code'],
                    'language_name': benchmark_data['language_name'],
                    'category': benchmark_data['category'],
                }
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Benchmark créé : {benchmark.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Benchmark existant : {benchmark.name}')
                )

            # Create test cases
            for test_data in benchmark_data['tests']:
                test_case, created = TestCase.objects.get_or_create(
                    benchmark=benchmark,
                    input_text=test_data['input_text'],
                    defaults={
                        'expected_output': test_data['expected_output'],
                        'context': test_data['context'],
                        'category': test_data.get('category', ''),
                        'difficulty': test_data.get('difficulty', 2),
                        'scoring_criteria': test_data.get('scoring_criteria', {}),
                        'tags': test_data.get('tags', []),
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'  Test créé : {test_case.input_text[:50]}...')
                    )

            # Update test count
            benchmark.update_test_count()

        self.stdout.write(
            self.style.SUCCESS('Benchmarks chargés avec succès !')
        )
