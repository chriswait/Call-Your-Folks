from .models import *
from callyourfolks.serializers import CallSerializer
from datetime import date, timedelta

def get_user_recommended_calls(user):
    today_date = date.today()
    overdue = []
    today = []
    soon = []
    for call in user.calls.filter(recommended=True):
        if (call.date < today_date and call.happened==False):
            overdue.append(CallSerializer(call).data)
        elif (call.date == today_date):
            today.append(CallSerializer(call).data)
        else:
            soon.append(CallSerializer(call).data)

    recommended_calls = {
        "overdue": overdue,
        "today": today,
        "soon": soon,
    }
    return recommended_calls
