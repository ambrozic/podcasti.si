from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from podcasts import sitemaps, views

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("health/", views.health, name="health"),
        path("", views.IndexView.as_view(), name="home"),
        path("vsi-podcasti/", views.AllPodcastsView.as_view(), name="all-podcasts"),
        path(
            "<slug:podcast_slug>/ep/<slug:episode_slug>/",
            views.EpisodeView.as_view(),
            name="episode",
        ),
        path(
            "<str:category_slug>-epizode/",
            views.EpisodeCategoryView.as_view(),
            name="latest-episodes-in-category",
        ),
        path("<slug:podcast_slug>/", views.PodcastView.as_view(), name="podcast"),
        path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps.sitemaps_dict},
            name="django.contrib.sitemaps.views.sitemap",
        ),
    ]
    + [url(r"^api/", include(views.router.urls))]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
