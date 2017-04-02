from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^not-a-disappointment-like-shreya/$', views.not_a_disappointment),
	url(r'^a-big-disappointment-just-like-shreya/$', views.disappointment),
	url(r'^$',views.render_page)
]