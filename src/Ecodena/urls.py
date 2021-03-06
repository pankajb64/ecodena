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
	#url(r'^postQuery/$', 'Ecodena.Query.views.postQuery'),
	url(r'^questions/(?P<questionID>[0-9]+)/$', 'Ecodena.Question.views.viewQuestionByID'),
	url(r'^submitSolution/(?P<questionID>[0-9]+)/$', 'Ecodena.Attempt.views.submitSolution'),
	url(r'^profile/$','Ecodena.User.views.viewProfile'),
	url(r'^profile/edit/$','Ecodena.User.views.editProfile'),
	url(r'^profile/(?P<username>.+)/$','Ecodena.User.views.viewProfileByID'),
	url(r'^solutions/$','Ecodena.Attempt.views.listSolutions'),
	url(r'^solutions/(?P<solutionID>[0-9]+)$','Ecodena.Attempt.views.viewSolution'),
	url(r'^login/$',  'Ecodena.Main.views.login'),
	url(r'^logout/$', 'Ecodena.Main.views.logout'),
	url(r'^accounts/change_password/$', 'django.contrib.auth.views.password_change',{'post_change_redirect' : '/accounts/change_password/done/' }),
    url(r'^accounts/change_password/done/', 'django.contrib.auth.views.password_change_done'),
	url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset',{'post_reset_redirect' : '/accounts/password/reset/done/'}),
	url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',{'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
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
	url(r'^problemSetter/viewProblems/$','Ecodena.ProblemSetter.views.ViewProblemSet'),
	url(r'^problemSetter/viewProblems/(?P<questionID>[0-9]+)$','Ecodena.ProblemSetter.views.ViewProblem'),
	url(r'^problemSetter/addProblem/$','Ecodena.ProblemSetter.views.UploadProblem'),
	url(r'^problemSetter/editProblem/(?P<qID>[0-9]+)/','Ecodena.ProblemSetter.views.EditProblem'),
	url(r'^problemSetter/deleteProblem/(?P<qID>[0-9]+)/','Ecodena.ProblemSetter.views.DeleteProblem'),
	url(r'^problemSetter/UploadProblem/$','Ecodena.ProblemSetter.views.UploadProblem'),
	#url(r'^notification/', include('notification.urls')),
	url(r'^ranking/$', 'Ecodena.User.views.generatePointsUser'),
	url(r'^rating/(?P<questionID>[0-9]+)/$', 'Ecodena.Question.views.generateRating'),
	url(r'^aboutUs/$','Ecodena.Main.views.AboutUs'),
	url(r'^editTestCase/(?P<caseID>[0-9]+)$','Ecodena.ProblemSetter.views.EditTestCase'),
	url(r'^addTestCase/(?P<questionID>[0-9]+)/$','Ecodena.ProblemSetter.views.AddTestCase'),
)








