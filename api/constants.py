from django.db import models
from django.utils.translation import ugettext_lazy as _


class ProfileTypes(models.TextChoices):
    plataform_user = ("plataform_user", _("Usuário da plataforma"))  # PERFIL QUE POSSUI USUÁRIO VINCULADO
    simple_customer = (
        "simple_customer",
        _("Cliente simples"),
    )  # CLIENTE COMUM VINCULADO A ALGUM PERFIL DE USUÁRIO


class States(models.TextChoices):
    ro = ("RO", _("Rondônia"))
    ac = ("AC", _("Acre"))
    am = ("AM", _("Amazonas"))
    rr = ("RR", _("Roraima"))
    pa = ("PA", _("Pará"))
    ap = ("AP", _("Amapá"))
    to = ("TO", _("Tocantins"))
    ma = ("MA", _("Maranhão"))
    pi = ("PI", _("Piauí"))
    ce = ("CE", _("Ceará"))
    rn = ("RN", _("Rio Grande do Norte"))
    pb = ("PB", _("Paraíba"))
    pe = ("PE", _("Pernambuco"))
    al = ("AL", _("Alagoas"))
    se = ("SE", _("Sergipe"))
    ba = ("BA", _("Bahia"))
    mg = ("MG", _("Minas Gerais"))
    es = ("ES", _("Espírito Santo"))
    rj = ("RJ", _("Rio de Janeiro"))
    sp = ("SP", _("São Paulo"))
    pr = ("PR", _("Paraná"))
    sc = ("SC", _("Santa Catarina"))
    rs = ("RS", _("Rio Grande do Sul"))
    ms = ("MS", _("Mato Grosso do Sul"))
    mt = ("MT", _("Mato Grosso"))
    go = ("GO", _("Goiás"))
    df = ("DF", _("Distrito Federal"))
