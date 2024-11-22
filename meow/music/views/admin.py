from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def admin_panel_view(request):
    context = {

    }

    return render(request, "music/admin.html", context)
