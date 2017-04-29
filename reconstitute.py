import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c9_django.settings")

import django
django.setup()
from polls.models import Quotes

Quotes.objects.get_or_create(quote_text="new quote", pub_date="2000-01-01T00:00:00+05:00")

# IDTyp.objects.get_or_create(abbr="SSN", desc="Social Security Number")
# IDTyp.objects.get_or_create(abbr="FBI", desc="FBI Number")
# IDTyp.objects.get_or_create(abbr="SCH", desc="School ID Card")
# IDTyp.objects.get_or_create(abbr="FSH", desc="Fishing License")