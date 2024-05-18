from django import template

register = template.Library()

@register.filter()

def censor(text):
    censored_words = ('хищениях', 'следователи', 'добавила', 'завершил', 'информацию')

    for i in text.split():
        if i.lower() in censored_words:
            text = text.replace(i, f"{i[0]}{'*' * (len(i) - 1)}")
    return text

