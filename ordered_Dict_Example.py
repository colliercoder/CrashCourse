from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['dan'] = 'python'
favorite_languages['jake'] = 'javascript'
favorite_languages['alejandra'] = 'wahts a language'
favorite_languages['jeff'] = 'sql'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print(favorite_languages)

