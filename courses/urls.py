from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from courses.views.homepage import HomePage
from courses.views.showpage import playvideo
from courses.views.signup_login import SignupView, LoginView, signout
from courses.views.checkout import Checkout, verify_payment
from courses.views.search import results
from courses.views.mycourses import Mycourseslist

urlpatterns = [
    path('', HomePage.as_view(), name='Homepage'),
    path('show/<slug>', playvideo, name="showpage"),
    path('checkout/<slug>', Checkout, name="check-out"),
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('results', results, name="search"),
    path('logout', signout, name="logout"),
    path('mycourses', Mycourseslist.as_view(), name="mycourseslist"),
    path('verify_payment', verify_payment, name='verify_payment'),
    path('forgot-password', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('password-reset', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='courses/forget.html'), name="password_reset_complete"),
    re_path(r'^files/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

handler404 = "courses.hand.error_404"
