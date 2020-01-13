from main_app.models import *
from django.core.management.base import BaseCommand
from testmaker import realec_grammar_exercises_without_mc as testmaker

class Command(BaseCommand):
    help = 'Fills database with questions generated from error annotations of texts'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--folder', type=str, help='Folder to process')
        parser.add_argument('-t', '--tag', nargs='+', type=str, help='Error tag to include')
        parser.add_argument('-s', '--strike', dest='strike', action='store_true', help='Whether to strike out wrong answers')
    
    def handle(self, *args, **kwargs):
        ## To add: check for duplicate documents:
        generate_questions(kwargs['folder'], kwargs['tag'], kwargs['strike'])
    
def generate_questions(folder, tags, strike, delete_downloaded=True):
    exercises = testmaker.download_folder_and_make_exercises(folder_name=folder,
    error_types=tags, file_output=False, moodle_output=False, make_two_variants=False,
    delete_downloaded=delete_downloaded)['short_answer']
    last_id = Question.objects.last().id
    if strike:
        questions = [Question(id=last_id+idx+1, question_text=ex[0].replace('<b>','<b><s>').replace('</b>', '</s></b>')
        ,error_tag=ex[3], question_type="short_answer", question_level=0) for idx, ex in enumerate(exercises)]
    else:
        questions = [Question(id=last_id+idx,question_text=ex[0], error_tag=ex[3],
        question_type="short_answer", question_level=0) for idx, ex in enumerate(exercises)]
    Question.objects.bulk_create(questions)
    answers=[Answer(question_id_id=q.id, answer_text=ans) for ex, q in zip(exercises, questions) for ans in ex[1]]
    Answer.objects.bulk_create(answers)