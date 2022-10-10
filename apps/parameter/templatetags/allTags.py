from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def static_cdn(url):
    if settings.CDN_ENABLED:
        url = static(url).replace(settings.AWS_S3_CUSTOM_DOMAIN, settings.AWS_S3_CDN_DOMAIN).replace('/static/', '/')
        return url
    else:
        return static(url)


@register.simple_tag
def changelanguage(path, lang):
    if path and lang:
        if lang == 'en':
            newPath = path.replace("/tr/", "/en/")
            newPath = newPath.replace("iletisim", "contact")
            newPath = newPath.replace("hakkimizda", "about")
            newPath = newPath.replace("teklif", "offer")
            newPath = newPath.replace("referanslar", "references")

        else:
            newPath = path.replace("/en/", "/tr/")
            newPath = newPath.replace("contact", "iletisim")
            newPath = newPath.replace("about", "hakkimizda")
            newPath = newPath.replace("offer", "teklif")
            newPath = newPath.replace("references", "referanslar")
        return newPath
    else:
        return path


@register.filter
def to_br(value):
    return value.replace("<br>", "")
