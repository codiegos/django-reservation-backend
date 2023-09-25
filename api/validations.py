from django.core.validators import RegexValidator

COLOR_VALIDATOR = RegexValidator(
        regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
        message='El color debe estar en el formato #FFFFFF o #FFF'
    )

PHONE_VALIDATOR = RegexValidator(
        regex=r'^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$',
        message='El numero de télefono debe estar en el formato +56912345678'
    )


