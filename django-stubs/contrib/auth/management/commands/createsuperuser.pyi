from django.core.management.base import BaseCommand

class NotRunningInTTYException(Exception): ...
class Command(BaseCommand): ...
