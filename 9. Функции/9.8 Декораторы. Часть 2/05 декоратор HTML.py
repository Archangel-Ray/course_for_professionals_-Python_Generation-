"""
Тег — элемент языка разметки, используемый для форматирования текста. Например, текст, заключённый между начальным
    тегом <small> и конечным тегом </small>, отображается с меньшим размером, чем основной текст, а текст между
    тегами <big> и </big> отображается с большим размером.

Реализуйте декоратор make_html(), который принимает один аргумент:

    tag — HTML-тег, например, del

Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
                также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
print('\nтест 1')


@make_html('del')
def get_text(text):
    return text


print(get_text('Python'))

# TEST_2:
print('\nтест 2')


@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text(text='decorators are so cool!'))

# TEST_3:
print('\nтест 3')


@make_html('small')
@make_html('mark')
@make_html('i')
@make_html('del')
def get_text(text):
    return text


print(get_text('ANRIANRIANRI'))

# TEST_4:
print('\nтест 4')


@make_html('mark')
@make_html('mark')
def get_text(text):
    return text * 2


print(get_text(text='doubleit'))

# TEST_5:
print('\nтест 5')


@make_html('mark')
@make_html('mark')
@make_html('mark')
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)
