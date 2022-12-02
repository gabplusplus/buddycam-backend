from django.urls import path
from . import views as v

app_name = 'members'

urlpatterns = [
    path('', v.MembersList.as_view(), name='memberslistcreate'),
    path('<int:pk>/', v.MembersDetail.as_view(), name='membersdetail'),
    path('<int:pk>/delete/', v.MembersDestroy.as_view(), name='membersdestroy'),
]