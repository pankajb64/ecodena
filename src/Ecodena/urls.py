from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
# Examples:
	url(r'^$', 'Ecodena.Main.views.home', name='home'),
	# url(r'^Ecodena/', include('Ecodena.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	url(r'^test/$', 'Ecodena.Main.views.sendmail'),

	url(r'^questions/$', 'Ecodena.Question.views.listQuestions'),
	url(r'^postQuery/$', 'Ecodena.Query.views.postQuery'),
	url(r'^questions/(?P<questionID>[0-9]+)/$', 'Ecodena.Question.views.viewQuestionByID'),
	url(r'^submitSolution/(?P<questionID>[0-9]+)/$', 'Ecodena.Attempt.views.submitSolution'),
	url(r'^profile/$','Ecodena.User.views.viewProfile'),
	url(r'^profile/edit/$','Ecodena.User.views.editProfile'),
	url(r'^profile/(?P<username>.+)/$','Ecodena.User.views.viewProfileByID'),
	url(r'^solutions/$','Ecodena.Attempt.views.listSolutions'),
	url(r'^solutions/(?P<solutionID>[0-9]+)/$','Ecodena.Attempt.views.viewSolution'),
	url(r'^login/$',  login),
    url(r'^logout/$', 'Ecodena.Main.views.logout'),
    url(r'^register/$', 'Ecodena.Main.views.register'),
	url(r'^recommendations/$','Ecodena.Recommendation.views.viewRecommendations'),
	url(r'^forum/', include('forum.urls')),
	#url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^wiki/', include('simplewiki.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^viewContest/$','Ecodena.Contest.views.listContests'),
	url(r'^viewContest/(?P<contestID>[0-9]+)$','Ecodena.Contest.views.listContestQuestion'),
	url(r'^viewContest/(?P<contestID>[0-9]+)/(?P<questionID>[0-9]+)/$','Ecodena.Contest.views.contestQuestion'),
	url(r'^holdContest/$','Ecodena.Contest.views.holdContest'),
	#url(r'^registerInContest/(?P<contestID>[0-9]+)$','Ecodena.Contest.views.registerInContest'),
)
