from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock



class About(Page):
    max_count = 1
    template = "about/about_page.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = []

    name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ForeignKey('wagtailimages.Image', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    addres = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("job_title"),
        FieldPanel("bio"),
        FieldPanel("avatar"),
        FieldPanel("email"),
        FieldPanel("phone"),
        FieldPanel("addres"),
        FieldPanel("linkedin"),
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("facebook")
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"